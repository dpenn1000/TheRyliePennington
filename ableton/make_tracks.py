#!/usr/bin/env python3
"""Generate humanized drum + bass MIDI clips for live backing tracks in Ableton.

No dependencies. Run:  python3 make_tracks.py
Output lands in ./clips/<song>/, one .mid per section per track (drums, bass, lights),
ready to drag into Session View clip slots.

To add a song, copy an entry in SONGS and change tempo, feel and chords.
Chords are one per bar: "G", "Em", "C/E" (slash = bass note), "D7", etc.
Write chords in chart shapes and set "transpose" to the capo fret; the bass sounds in the real key.
Set "bass": False on a song when Rylie plays bass live; only drums and lights are written.
"""
import os
import random
import struct

PPQ = 480
BAR = PPQ * 4
E8 = PPQ // 2
E16 = PPQ // 4

# General MIDI drum map (matches Ableton acoustic kits, MT Power Drum Kit, LABS, etc.)
KICK, STICK, SNARE, HAT, PEDAL_HAT, OPEN_HAT = 36, 37, 38, 42, 44, 46
FLOOR_TOM, LOW_TOM, MID_TOM, HIGH_TOM, CRASH, RIDE = 43, 45, 47, 50, 49, 51

NOTE = {"C": 0, "C#": 1, "Db": 1, "D": 2, "D#": 3, "Eb": 3, "E": 4, "F": 5,
        "F#": 6, "Gb": 6, "G": 7, "G#": 8, "Ab": 8, "A": 9, "A#": 10, "Bb": 10, "B": 11}

SONGS = [
    # Chords are written in chart shapes, exactly as they appear in the Lyrics and Chords
    # charts. "transpose" is the capo: it moves the bass to the sounding key.
    # Bar counts are estimates from the lyric lines. Fix them at rehearsal and re-run.
    {
        "name": "02-halfway-gone",
        "tempo": 104,            # try 100 and 108 at rehearsal
        "feel": "straight",
        "transpose": 2,          # G shapes, capo 2, sounds in A
        "verse_stick": True,     # cross-stick verses, snare from the pre-chorus on
        # Song order from the chart. The outro's C C C G is the "halfway gone x3" tag.
        "form": ["1-intro", "2-verse", "3-prechorus", "4-chorus", "2-verse", "3-prechorus", "4-chorus",
                 "5-bridge", "4-chorus", "6-outro"],
        "sections": {
            "1-intro":     {"chords": ["G", "C", "Em", "D"], "style": "light"},
            "2-verse":     {"chords": ["G", "C", "Em", "D"] * 2, "style": "verse"},
            "3-prechorus": {"chords": ["Em", "C", "G", "D", "D", "D"], "style": "verse", "snare": True},
            "4-chorus":    {"chords": ["G", "C", "Em", "D"] * 2 + ["C", "G", "G", "G"], "style": "chorus"},
            "5-bridge":    {"chords": ["Am", "G", "Am", "D", "Am", "C", "C", "D"], "style": "light"},
            "6-outro":     {"chords": ["C", "C", "C", "G"], "style": "ending"},
        },
    },
    {
        "name": "06-choosin-texas",
        "tempo": 110,
        "feel": "straight",
        "transpose": 1,          # C shapes, capo 1, sounds in Db
        "sections": {
            "1-intro":  {"chords": ["Dm7", "C", "C", "C", "Dm7", "F", "C", "C"], "style": "light"},
            "2-verse":  {"chords": ["C", "Dm7", "C", "C", "Dm7", "Dm7", "C", "C", "F", "F", "G", "G"],
                         "style": "verse"},
            "3-chorus": {"chords": ["F", "F", "C", "C", "Dm7", "Dm7", "G", "G",
                                    "Fmaj7", "Fmaj7", "Am7", "Am7", "F", "F", "G", "C"], "style": "chorus"},
            "4-bridge": {"chords": ["F", "G", "F/A", "G/B", "F", "G", "Dm7", "G"], "style": "light"},
            "5-outro":  {"chords": ["Dm", "C", "Dm", "F", "C"], "style": "ending"},
        },
    },
    {
        "name": "07-kiss-me",
        "tempo": 100,
        "feel": "straight",
        "transpose": 1,          # D shapes, capo 1, sounds in Eb
        "sections": {
            "1-intro":  {"chords": ["D", "Dmaj7", "D7", "Dmaj7"] * 2, "style": "light"},
            "2-verse":  {"chords": ["D", "Dmaj7", "D7", "Dmaj7", "D", "Dmaj7", "D7", "G"], "style": "verse"},
            "3-chorus": {"chords": ["Em", "A", "D", "Bm", "Em", "A", "D", "D7",
                                    "Em", "A", "D", "D/C#", "Bm", "G", "A", "D"], "style": "chorus"},
            "4-bridge": {"chords": ["Em", "A", "D", "Bm", "Em", "A", "D", "D7"], "style": "verse"},  # the solo
            "5-outro":  {"chords": ["Dmaj7", "D7", "Dmaj7", "D"], "style": "ending"},
        },
    },
    {
        "name": "10-paper-stars",
        "tempo": 88,
        "feel": "straight",
        "transpose": 1,          # C shapes, capo 1, sounds in Db
        "sections": {
            "1-intro":     {"chords": ["C", "Am", "F", "G"], "style": "light"},
            "2-verse":     {"chords": ["C", "Am", "F", "G"] * 2, "style": "verse"},
            "3-prechorus": {"chords": ["Am", "C", "Am", "C", "F", "C", "F", "G"], "style": "light"},
            "4-chorus":    {"chords": ["C", "F", "G", "F", "Am", "F", "G", "F",
                                       "C", "F", "G", "F", "Am", "F", "G", "C"], "style": "chorus"},
            "5-bridge":    {"chords": ["F", "Am", "F", "C", "F", "Am", "F", "C", "F", "Am", "C", "G"],
                            "style": "light"},
            "6-outro":     {"chords": ["F", "G", "C", "C"], "style": "ending"},
        },
    },
]


# ---------------------------------------------------------------- MIDI writer
def vlq(n):
    out = [n & 0x7F]
    n >>= 7
    while n:
        out.append((n & 0x7F) | 0x80)
        n >>= 7
    return bytes(reversed(out))


def track_chunk(events, name, tempo, end):
    """events: list of (tick, note, velocity, length, channel). end = clip length in ticks."""
    raw = []
    raw.append((0, b"\xff\x03" + vlq(len(name)) + name.encode()))
    if tempo:
        us = int(60_000_000 / tempo)
        raw.append((0, b"\xff\x51\x03" + us.to_bytes(3, "big")))
        raw.append((0, b"\xff\x58\x04\x04\x02\x18\x08"))
    for t, n, v, ln, ch in events:
        t = max(0, min(t, end - E16))
        raw.append((t, bytes([0x90 | ch, n, max(1, min(127, v))])))
        # never let a note ring past the loop point, or Ableton adds an extra bar
        raw.append((min(t + ln, end), bytes([0x80 | ch, n, 0])))
    # note-offs sort before note-ons at the same tick
    raw.sort(key=lambda e: (e[0], 0 if e[1][0] & 0xF0 == 0x80 else 1))
    data, last = b"", 0
    for t, msg in raw:
        data += vlq(t - last) + msg
        last = t
    data += vlq(end - last) + b"\xff\x2f\x00"
    return b"MTrk" + struct.pack(">I", len(data)) + data


def write_mid(path, events, name, tempo, bars):
    header = b"MThd" + struct.pack(">IHHH", 6, 0, 1, PPQ)
    with open(path, "wb") as f:
        f.write(header + track_chunk(events, name, tempo, bars * BAR))


# ---------------------------------------------------------------- humanizing
class Human:
    """Small, drummer-like imperfections. Seeded so output is repeatable."""

    def __init__(self, seed):
        self.r = random.Random(seed)

    def t(self, tick, push=0, spread=6):
        # push > 0 = late (laid back), < 0 = early (driving)
        return int(tick + push + self.r.gauss(0, spread))

    def v(self, vel, spread=6):
        return int(vel + self.r.gauss(0, spread))

    def chance(self, p):
        return self.r.random() < p


def swing(pos_in_beat, feel):
    """Shift offbeat 8ths later for a shuffle (triplet swing ~ 66%)."""
    if feel == "shuffle" and pos_in_beat == E8:
        return int(PPQ * 2 / 3)
    return pos_in_beat


# ---------------------------------------------------------------- drums
def drum_bar(h, bar, style, feel, fill=False, first=False, last_bar=False, stick=False):
    ev = []
    b0 = bar * BAR

    def hit(tick, note, vel, push=0, spread=6):
        ev.append((h.t(b0 + tick, push, spread), note, h.v(vel), E16, 9))

    shuffle = feel == "shuffle"
    loud = {"light": 0.75, "verse": 0.9, "chorus": 1.0, "ending": 1.0}[style]

    if style == "ending" and last_bar:
        hit(0, KICK, 118)
        hit(0, CRASH, 120)
        hit(0, SNARE, 100, push=4)
        return ev

    if first and style in ("chorus", "ending"):
        hit(0, CRASH, int(112 * loud))

    beats = 3 if fill else 4
    for beat in range(beats):
        for sub in (0, E8):
            pos = beat * PPQ + swing(sub, feel)
            if style == "light":
                # sidestick + pedal hat: quiet, leaves room for vocals
                if sub == 0:
                    hit(pos, PEDAL_HAT if beat % 2 == 0 else HAT, int(70 * loud), spread=8)
            else:
                cymbal = RIDE if style == "chorus" and shuffle else HAT
                accent = 92 if sub == 0 else 68
                if sub == 0 and beat in (0, 2):
                    accent += 8
                hit(pos, cymbal, int(accent * loud), spread=7)

    # backbeat, slightly behind the grid for a relaxed feel
    for beat in (1, 3):
        if fill and beat == 3:
            continue
        if style == "light" or stick:
            hit(beat * PPQ, STICK, int(88 * loud), push=6)
        else:
            hit(beat * PPQ, SNARE, int(108 * loud), push=8)

    # kick pattern, slightly ahead to drive
    kicks = [0, 2 * PPQ]
    if style in ("verse", "chorus"):
        kicks.append(2 * PPQ + swing(E8, feel))
        if h.chance(0.35):
            kicks.append(swing(E8, feel) + (0 if shuffle else 0))
    for k in kicks:
        if fill and k >= 3 * PPQ:
            continue
        hit(k, KICK, int((105 if k in (0, 2 * PPQ) else 88) * loud), push=-3)

    # ghost notes on the snare, the thing that makes it sound played
    if style in ("verse", "chorus") and not stick:
        for beat in range(4):
            for g in ((E16 * 3,) if not shuffle else (int(PPQ * 2 / 3) + 40,)):
                if h.chance(0.28) and not (fill and beat == 3):
                    hit(beat * PPQ + g, SNARE, 34, push=4, spread=10)

    if fill:
        ev += drum_fill(h, b0 + 3 * PPQ, style, feel)
    return ev


def drum_fill(h, start, style, feel):
    """Last beat of the bar: a short tom or snare run."""
    ev = []
    if style == "light":
        pattern = [(0, STICK, 80), (E8, STICK, 90)]
    elif h.chance(0.5):
        pattern = [(0, SNARE, 95), (E16, SNARE, 70), (E8, HIGH_TOM, 100), (3 * E16, FLOOR_TOM, 110)]
    else:
        pattern = [(0, HIGH_TOM, 100), (E16, MID_TOM, 95), (E8, LOW_TOM, 100), (3 * E16, FLOOR_TOM, 112)]
    if feel == "shuffle":
        third = PPQ // 3
        pattern = [(i * third, n, v) for i, (_, n, v) in enumerate(pattern[:3])]
    for off, note, vel in pattern:
        ev.append((h.t(start + off, 0, 5), note, h.v(vel, 5), E16, 9))
    ev.append((h.t(start, -3), KICK, h.v(90), E16, 9))
    return ev


def drums(section, feel, seed, verse_stick=False):
    """verse_stick: cross-stick backbeat in verse-style sections (Americana/country verses)."""
    h = Human(seed)
    stick = verse_stick and section["style"] == "verse" and not section.get("snare")
    n = len(section["chords"])
    ev = []
    for bar in range(n):
        last = bar == n - 1
        fill = last and section["style"] != "ending"
        ev += drum_bar(h, bar, section["style"], feel, fill=fill, first=bar == 0, last_bar=last, stick=stick)
    return ev


def fill_clip(feel, seed, style="verse"):
    h = Human(seed)
    return drum_bar(h, 0, style, feel, fill=True)


# ---------------------------------------------------------------- bass
def parse_chord(sym, transpose=0):
    bass = None
    if "/" in sym:
        sym, bass = sym.split("/")
    root = sym[:2] if len(sym) > 1 and sym[1] in "#b" else sym[:1]
    minor = sym[len(root):].startswith("m") and not sym[len(root):].startswith("maj")
    r = (NOTE[root] + transpose) % 12
    return r, minor, (NOTE[bass] + transpose) % 12 if bass else r


# Toontrack's EZbass puts the open low E string on MIDI 40 and uses 21-32 for keyswitches
# (ghost notes, slides, legato), so the General MIDI bass octave (28-39) fires slides instead
# of notes. Stay in 40-51.
BASS_LOW = 40


def bass_pitch(pc):
    """Place a pitch class in the bass range, low E string (40) up to D# (51)."""
    p = BASS_LOW - 4 + pc
    return p + 12 if p < BASS_LOW else p


def bass(section, feel, seed, transpose=0):
    h = Human(seed + 1000)
    chords = section["chords"]
    style = section["style"]
    ev = []
    for bar, sym in enumerate(chords):
        r, minor, low = parse_chord(sym, transpose)
        root = bass_pitch(low)
        fifth = bass_pitch((r + 7) % 12)
        third = bass_pitch((r + (3 if minor else 4)) % 12)
        nxt = parse_chord(chords[(bar + 1) % len(chords)], transpose)[2]
        target = bass_pitch(nxt)
        # approach note: a half step below or above the next root
        approach = target - 1 if h.chance(0.6) and target > BASS_LOW else target + 1
        b0 = bar * BAR
        last = bar == len(chords) - 1

        def note(tick, p, vel, length):
            ev.append((h.t(b0 + tick, -2, 5), p, h.v(vel, 5), length, 0))

        if style == "ending" and last:
            note(0, root, 105, BAR - E8)
            continue
        if style == "light":
            note(0, root, 88, 2 * PPQ - 40)
            note(2 * PPQ, fifth if h.chance(0.5) else root, 80, 2 * PPQ - 40)
            continue
        sw = swing(E8, feel)
        if style == "verse":
            note(0, root, 100, PPQ - 30)
            note(PPQ + sw, root, 72, E8 - 20)
            note(2 * PPQ, fifth, 92, PPQ - 30)
            note(3 * PPQ, root, 85, E8)
            note(3 * PPQ + sw, approach if not last else root, 80, E8 - 20)
        else:  # chorus: driving 8ths with movement
            line = [root, root, root, third, fifth, fifth, root, approach]
            for i, p in enumerate(line):
                beat, off = divmod(i, 2)
                pos = beat * PPQ + (sw if off else 0)
                vel = 100 if off == 0 else 78
                note(pos, p, vel, E8 - 30)
    return ev


# ---------------------------------------------------------------- lights
# One note on the downbeat of each section. ONYX maps each note to a cuelist.
# Ableton names: C3 = 60. Keep this table in sync with LIGHTING.md.
LIGHT_CUES = {
    "intro": 60,    # C3  warm, low intensity
    "verse": 62,    # D3  warm wash
    "prechorus": 63, # D#3 verse look, a step brighter
    "chorus": 64,   # E3  full, brighter color
    "bridge": 65,   # F3  cool, moody
    "outro": 67,    # G3  build to full, then hold
    "fill": 69,     # A3  quick flash / bump
    "blackout": 72, # C4  all off
}


def lights(sec_name):
    kind = sec_name.split("-", 1)[1]
    return [(0, LIGHT_CUES[kind], 100, E8, 0)]


# ---------------------------------------------------------------- main
def main():
    here = os.path.dirname(os.path.abspath(__file__))
    for s, song in enumerate(SONGS):
        out = os.path.join(here, "clips", song["name"])
        os.makedirs(out, exist_ok=True)
        parts = {}
        for i, (sec_name, sec) in enumerate(song["sections"].items()):
            seed = s * 100 + i
            bars = len(sec["chords"])
            d = drums(sec, song["feel"], seed, song.get("verse_stick", False))
            b = bass(sec, song["feel"], seed, song.get("transpose", 0))
            write_mid(os.path.join(out, f"{sec_name}-drums.mid"), d, f"{sec_name} drums", song["tempo"], bars)
            if song.get("bass", True):
                write_mid(os.path.join(out, f"{sec_name}-bass.mid"), b, f"{sec_name} bass", song["tempo"], bars)
            write_mid(os.path.join(out, f"{sec_name}-lights.mid"), lights(sec_name), f"{sec_name} lights",
                      song["tempo"], bars)
            parts[sec_name] = (d, b, bars)
        # Full song: the sections in song order ("form"), or each section once.
        full_d, full_b, full_l, offset = [], [], [], 0
        for sec_name in song.get("form", list(song["sections"])):
            d, b, bars = parts[sec_name]
            full_d += [(t + offset, *rest) for t, *rest in d]
            full_b += [(min(t, bars * BAR - E16) + offset, n, v, min(ln, bars * BAR - t), c)
                       for t, n, v, ln, c in b]
            full_l += [(t + offset, *rest) for t, *rest in lights(sec_name)]
            offset += bars * BAR
        fill_no = len(song["sections"]) + 1
        write_mid(os.path.join(out, f"{fill_no}-fill-drums.mid"), fill_clip(song["feel"], s * 100 + 50),
                  "fill", song["tempo"], 1)
        write_mid(os.path.join(out, f"{fill_no}-fill-lights.mid"), [(0, LIGHT_CUES["fill"], 100, E8, 0)],
                  "fill lights", song["tempo"], 1)
        total = offset // BAR
        write_mid(os.path.join(out, "0-full-song-drums.mid"), full_d, "full drums", song["tempo"], total)
        if song.get("bass", True):
            write_mid(os.path.join(out, "0-full-song-bass.mid"), full_b, "full bass", song["tempo"], total)
        write_mid(os.path.join(out, "0-full-song-lights.mid"), full_l, "full lights", song["tempo"], total)
        print(f"{song['name']}: {song['tempo']} BPM, {song['feel']} -> {out}")


if __name__ == "__main__":
    main()
