#!/usr/bin/env python3
"""Build an Ableton Live Set (.als) for one song from the clips make_tracks.py wrote.

No dependencies. Run:  python3 make_set.py 02-halfway-gone "E:/Daddy Long Legs/Songs/Halfway Gone/Halfway Gone.als"

The set has three MIDI tracks (Drums, Bass, Lights), one scene per section in song order with
the full-song take last, the song's tempo, and every clip looping. It starts from template.als,
an empty set saved by Live 12.4.6, so it needs Live 12.4.6 or newer.

Instruments are not loaded: drag EZdrummer 3 onto Drums and EZbass onto Bass, then save.
After that, re-run with --update on the saved set to refresh clips without losing the instruments.
Lights needs its MIDI To set to the loopMIDI "Lights" port (see LIGHTING.md).
"""
import argparse
import gzip
import os
import re
import sys
from xml.sax.saxutils import escape

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from make_tracks import SONGS  # noqa: E402

HERE = os.path.dirname(os.path.abspath(__file__))
# An empty set saved by Live 12.4.6. Live's own DefaultLiveSet.als is saved by an older 12.x and
# comes up "corrupt (non-unique Pointee IDs)" once clips are added, so build from this instead.
# Re-save it from a newer Live (File > New Live Set, Save As) if the laptop runs a newer version.
TEMPLATE = os.path.join(HERE, "template.als")
TRACKS = [("Drums", "drums", 1), ("Bass", "bass", 13), ("Lights", "lights", 58)]  # name, file suffix, colour
SECTION_NAMES = {"prechorus": "Pre-Chorus", "full-song": "Full Song"}


# ---------------------------------------------------------------- MIDI reader
def read_mid(path):
    """Return (notes, length_beats). notes = [(start_beats, dur_beats, pitch, velocity)]."""
    data = open(path, "rb").read()
    ppq = int.from_bytes(data[12:14], "big")
    pos, notes, end = 14, [], 0
    while pos < len(data):
        size = int.from_bytes(data[pos + 4:pos + 8], "big")
        trk, pos = data[pos + 8:pos + 8 + size], pos + 8 + size
        i = t = 0
        status = 0
        on = {}
        while i < len(trk):
            d = 0
            while True:
                b = trk[i]
                i += 1
                d = (d << 7) | (b & 0x7F)
                if b < 0x80:
                    break
            t += d
            if trk[i] == 0xFF:
                kind, i = trk[i + 1], i + 2
                ln = 0
                while True:
                    b = trk[i]
                    i += 1
                    ln = (ln << 7) | (b & 0x7F)
                    if b < 0x80:
                        break
                i += ln
                if kind == 0x2F:
                    end = max(end, t)
                continue
            if trk[i] & 0x80:
                status, i = trk[i], i + 1
            hi = status & 0xF0
            if hi in (0x80, 0x90):
                n, v, i = trk[i], trk[i + 1], i + 2
                if hi == 0x90 and v > 0:
                    on.setdefault(n, []).append((t, v))
                elif on.get(n):
                    s, sv = on[n].pop(0)
                    notes.append((s / ppq, max(t - s, 1) / ppq, n, sv))
            elif hi in (0xC0, 0xD0):
                i += 1
            else:
                i += 2
    return notes, end / ppq


# ---------------------------------------------------------------- XML pieces
def midi_clip(name, notes, length, color):
    keys = {}
    for s, d, n, v in sorted(notes):
        keys.setdefault(n, []).append((s, d, v))
    note_id, kt = 1, []
    for k, pitch in enumerate(sorted(keys)):
        ev = []
        for s, d, v in keys[pitch]:
            ev.append(f'<MidiNoteEvent Time="{s:g}" Duration="{d:g}" Velocity="{v}" OffVelocity="64" '
                      f'NoteId="{note_id}" />')
            note_id += 1
        kt.append(f'<KeyTrack Id="{k}"><Notes>{"".join(ev)}</Notes><MidiKey Value="{pitch}" /></KeyTrack>')
    L = f"{length:g}"
    return f"""<MidiClip Id="0" Time="0">
<LomId Value="0" /><LomIdView Value="0" /><CurrentStart Value="0" /><CurrentEnd Value="{L}" />
<Loop><LoopStart Value="0" /><LoopEnd Value="{L}" /><StartRelative Value="0" /><LoopOn Value="true" />
<OutMarker Value="{L}" /><HiddenLoopStart Value="0" /><HiddenLoopEnd Value="{L}" /></Loop>
<Name Value="{escape(name)}" /><Annotation Value="" /><Color Value="{color}" />
<LaunchMode Value="0" /><LaunchQuantisation Value="0" />
<TimeSignature><TimeSignatures><RemoteableTimeSignature Id="0"><Numerator Value="4" />
<Denominator Value="4" /><Time Value="0" /></RemoteableTimeSignature></TimeSignatures></TimeSignature>
<Envelopes><Envelopes /></Envelopes>
<ScrollerTimePreserver><LeftTime Value="0" /><RightTime Value="{L}" /></ScrollerTimePreserver>
<TimeSelection><AnchorTime Value="0" /><OtherTime Value="0" /></TimeSelection>
<Legato Value="false" /><Ram Value="false" /><GrooveSettings><GrooveId Value="-1" /></GrooveSettings>
<Disabled Value="false" /><VelocityAmount Value="0" />
<FollowAction><FollowTime Value="4" /><IsLinked Value="true" /><LoopIterations Value="1" />
<FollowActionA Value="4" /><FollowActionB Value="0" /><FollowChanceA Value="100" />
<FollowChanceB Value="0" /><JumpIndexA Value="1" /><JumpIndexB Value="1" />
<FollowActionEnabled Value="false" /></FollowAction>
<Grid><FixedNumerator Value="1" /><FixedDenominator Value="16" /><GridIntervalPixel Value="20" />
<Ntoles Value="2" /><SnapToGrid Value="true" /><Fixed Value="false" /></Grid>
<FreezeStart Value="0" /><FreezeEnd Value="0" /><IsWarped Value="true" /><TakeId Value="0" />
<IsInKey Value="false" /><ScaleInformation><Root Value="0" /><Name Value="0" /></ScaleInformation>
<AutomationEnvelopesListWrapper LomId="0" />
<Notes><KeyTracks>{"".join(kt)}</KeyTracks>
<PerNoteEventStore><EventLists /></PerNoteEventStore><NoteProbabilityGroups />
<ProbabilityGroupIdGenerator><NextId Value="1" /></ProbabilityGroupIdGenerator>
<NoteIdGenerator><NextId Value="{note_id}" /></NoteIdGenerator></Notes>
<BankSelectCoarse Value="-1" /><BankSelectFine Value="-1" /><ProgramChange Value="-1" />
<NoteEditorFoldInZoom Value="-1" /><NoteEditorFoldInScroll Value="0" />
<NoteEditorFoldOutZoom Value="-1" /><NoteEditorFoldOutScroll Value="0" />
<NoteEditorFoldScaleZoom Value="-1" /><NoteEditorFoldScaleScroll Value="0" />
<NoteSpellingPreference Value="0" /><AccidentalSpellingPreference Value="3" />
<PreferFlatRootNote Value="false" />
<ExpressionGrid><FixedNumerator Value="1" /><FixedDenominator Value="16" />
<GridIntervalPixel Value="20" /><Ntoles Value="2" /><SnapToGrid Value="false" /><Fixed Value="false" />
</ExpressionGrid></MidiClip>"""


def clip_slots(clips):
    out = []
    for i, clip in enumerate(clips):
        value = f"<Value>{clip}</Value>" if clip else "<Value />"
        out.append(f'<ClipSlot Id="{i}"><LomId Value="0" /><ClipSlot>{value}</ClipSlot>'
                   f'<HasStop Value="true" /><NeedRefreeze Value="true" /></ClipSlot>')
    return "<ClipSlotList>" + "".join(out) + "</ClipSlotList>"


# Follow action codes, in Live's menu order: No Action 0, Stop 1, Play Again 2, Previous 3, Next 4.
# Next = 4 matches Live's own demo sets, which chain scenes with it.
NEXT, STOP = 4, 1


def scene(i, name, tempo, follow=None):
    """follow = (beats, action): after that many beats, launch the next scene (NEXT) or stop (STOP)."""
    beats, action = follow or (4, NEXT)
    on = "true" if follow else "false"
    return f"""<Scene Id="{i}"><FollowAction><FollowTime Value="{beats:g}" /><IsLinked Value="false" />
<LoopIterations Value="1" /><FollowActionA Value="{action}" /><FollowActionB Value="0" />
<FollowChanceA Value="100" /><FollowChanceB Value="0" /><JumpIndexA Value="0" /><JumpIndexB Value="0" />
<FollowActionEnabled Value="{on}" /></FollowAction><Name Value="{escape(name)}" /><Annotation Value="" />
<Color Value="-1" /><Tempo Value="{tempo}" /><IsTempoEnabled Value="false" />
<TimeSignatureId Value="201" /><IsTimeSignatureEnabled Value="false" /><LomId Value="0" />
<ClipSlotsListWrapper LomId="0" /></Scene>"""


def song_clips(clip_dir, suffix, stems, names, color):
    clips = []
    for stem, label in zip(stems, names):
        path = os.path.join(clip_dir, f"{stem}-{suffix}.mid")
        if os.path.exists(path):
            notes, length = read_mid(path)
            clips.append(midi_clip(f"{label} {suffix}", notes, length, color))
        else:
            clips.append(None)
    return clips


def stamp_tracks(x, clip_dir, stems, names):
    """Turn the template's MIDI tracks into Drums, Bass and Lights with their clips."""
    # The template has two MIDI tracks, two audio tracks and two returns. Keep one MIDI track as
    # the pattern, drop the rest, and stamp out Drums, Bass and Lights from it.
    x = re.sub(r"\s*<AudioTrack Id=.*?</AudioTrack>", "", x, flags=re.S)
    tracks = re.findall(r"<MidiTrack Id=.*?</MidiTrack>", x, flags=re.S)
    pattern = tracks[0]
    x = x.replace(tracks[1], "")
    next_id = int(re.search(r'<NextPointeeId Value="(\d+)"', x).group(1))

    built = []
    for n, (tname, suffix, color) in enumerate(TRACKS):
        t = pattern
        if n:
            def renumber(m):
                nonlocal next_id
                next_id += 1
                return f'<{m.group(1)} Id="{next_id - 1}"'
            # Covers AutomationTarget, the *ModulationTargets, Pointee and ControllerTargets.0-130.
            t = re.sub(r'<([\w.]*(?:Target|Pointee)[\w.]*) Id="\d+"', renumber, t)
            # Track Ids share the Pointee Id space, so they come from the same counter.
            t = re.sub(r'^<MidiTrack Id="\d+"', f'<MidiTrack Id="{next_id}"', t)
            next_id += 1
        t = re.sub(r'<EffectiveName Value="[^"]*" />', f'<EffectiveName Value="{tname}" />', t, count=1)
        t = re.sub(r'<UserName Value="[^"]*" />', f'<UserName Value="{tname}" />', t, count=1)
        t = re.sub(r'(</Name>\s*<Color Value=")\d+', rf"\g<1>{color}", t, count=1)
        clips = song_clips(clip_dir, suffix, stems, names, color)
        t = re.sub(r"<ClipSlotList>.*?</ClipSlotList>", lambda m: clip_slots(clips), t, count=1, flags=re.S)
        built.append(t)
    x = x.replace(pattern, "\n".join(built))
    return re.sub(r'<NextPointeeId Value="\d+"', f'<NextPointeeId Value="{next_id + 1}"', x, count=1)


def refresh_tracks(x, clip_dir, stems, names, path):
    """Swap the Session clips on the Drums, Bass and Lights tracks of an existing set."""
    for tname, suffix, color in TRACKS:
        m = re.search(rf'<MidiTrack Id=(?:(?!</MidiTrack>).)*?<UserName Value="{tname}" />.*?</MidiTrack>',
                      x, flags=re.S)
        if not m:
            sys.exit(f"no track named {tname} in {path}")
        clips = song_clips(clip_dir, suffix, stems, names, color)
        # The first clip slot list is the Session clips; the second belongs to Freeze.
        t = re.sub(r"<ClipSlotList>.*?</ClipSlotList>", lambda _: clip_slots(clips), m.group(0),
                   count=1, flags=re.S)
        x = x[:m.start()] + t + x[m.end():]
    return x


def build(song_name, out_path, template=None, update=False):
    """update=True rewrites the clips, scenes and tempo of the existing set at out_path and keeps
    everything else, including the instruments and their sounds."""
    song = next(s for s in SONGS if s["name"] == song_name)
    clip_dir = os.path.join(HERE, "clips", song_name)
    x = gzip.open(out_path if update else (template or TEMPLATE), "rb").read().decode("utf-8")

    # One scene per section. With a "form", the scenes run in song order (Verse 1, Verse 2...) and
    # each one launches the next when it ends, so launching the first scene plays the song. Sections
    # outside the form (the fill) and the full-song take follow, with no follow action.
    all_stems = sorted({f.rsplit("-", 1)[0] for f in os.listdir(clip_dir) if f.endswith(".mid")})
    label = {st: SECTION_NAMES.get(st.split("-", 1)[1], st.split("-", 1)[1].replace("-", " ").title())
             for st in all_stems}
    form = song.get("form")
    stems, names, follows = [], [], []
    if form:
        seen = {}
        for n, st in enumerate(form):
            seen[st] = seen.get(st, 0) + 1
            repeats = form.count(st) > 1
            names.append(f"{label[st]} {seen[st]}" if repeats else label[st])
            stems.append(st)
            _, length = read_mid(os.path.join(clip_dir, f"{st}-drums.mid"))
            follows.append((length, NEXT if n < len(form) - 1 else STOP))
    for st in all_stems:
        if st not in stems and not st.startswith("0-"):
            stems.append(st), names.append(label[st]), follows.append(None)
    for st in all_stems:
        if st.startswith("0-"):
            stems.append(st), names.append(label[st]), follows.append(None)

    if update:
        x = refresh_tracks(x, clip_dir, stems, names, out_path)
    else:
        x = stamp_tracks(x, clip_dir, stems, names)

    # Any other clip slot lists (returns, main, freeze) must match the scene count.
    x = re.sub(r"<ClipSlotList>(?:(?!</ClipSlotList>).)*?</ClipSlotList>",
               lambda m: m.group(0) if "<MidiClip" in m.group(0) else clip_slots([None] * len(stems)),
               x, flags=re.S)
    x = re.sub(r"<Scenes>.*?</Scenes>",
               "<Scenes>" + "".join(scene(i, nm, song["tempo"], fo)
                                 for i, (nm, fo) in enumerate(zip(names, follows))) + "</Scenes>",
               x, count=1, flags=re.S)
    x = re.sub(r'(<Tempo>\s*<LomId Value="0" />\s*<Manual Value=")[\d.]+', rf'\g<1>{song["tempo"]}', x, count=1)
    # The main track also holds a tempo automation envelope whose one event overrides Manual.
    tempo_target = re.search(r'<Tempo>.*?<AutomationTarget Id="(\d+)"', x, flags=re.S).group(1)
    x = re.sub(rf'(<PointeeId Value="{tempo_target}" />.*?<FloatEvent Id="0" Time="[^"]*" Value=")[\d.]+',
               rf'\g<1>{song["tempo"]}', x, count=1, flags=re.S)

    os.makedirs(os.path.dirname(os.path.abspath(out_path)), exist_ok=True)
    with gzip.open(out_path, "wb") as f:
        f.write(x.encode("utf-8"))
    print(f"{song_name}: {len(stems)} scenes ({', '.join(names)}), {song['tempo']} BPM -> {out_path}")


if __name__ == "__main__":
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("song", help="song folder under clips/, e.g. 02-halfway-gone")
    ap.add_argument("out", help="path of the .als to write")
    ap.add_argument("--template", help="an empty .als to start from (defaults to template.als)")
    ap.add_argument("--update", action="store_true",
                    help="refresh the clips in the existing set at OUT, keeping its instruments")
    a = ap.parse_args()
    build(a.song, a.out, a.template, a.update)
