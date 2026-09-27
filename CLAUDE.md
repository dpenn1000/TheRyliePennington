# Daddy Long Legs: live rig project

Context for Claude sessions working in this repo. Read this first.

## Who and what

- **Daddy Long Legs** is a daddy-daughter acoustic duo: the dad (repo owner, dpenn1000) and his daughter **Rylie Pennington**. Websites: daddylonglegsband.com and ryliepennington.com.
- **Rylie** (13) sings and plays **guitar and bass guitar**, stars as the lead in the feature film *Not My Dog* (streaming since Sept 11, 2026; see `docs/RESEARCH.md`), has musical theatre credits, and sings the National Anthem at sporting events. The band writes originals and plays live gigs.
- **Consequence for the rig:** on songs where Rylie plays bass, the backing track should be drums only. Set `"bass": False` on that song in `make_tracks.py`. **As of Sept 26, 2026 nobody plays bass live, so every song gets a bass track.** Guest drummers or bassists sometimes sit in, so the drums and bass tracks each get a live on/off switch (track activator, mapped to a key or pedal). Build both tracks for every song; switching happens on stage, not in the generator.
- The dad already uses **Digital Performer (DP)** for writing and recording and is new to Ableton.
- **Goal:** live drum and bass backing tracks that sound natural and follow the band. Sections loop until the band moves on, so a verse can be stretched and a bridge skipped on stage. Lighting follows the same section changes.
- **Next gig:** Arizona State Fair. The fair runs **Oct 1 to Nov 1, 2026, Thursday to Sunday**. The band plays the fair's first weekend, so `docs/GIG-PLAN.md`'s tight plan applies (4 songs with tracks, lights on ONYX).
  - Gig date: **Sunday, October 4, 2026, 1:00 to 2:00 pm**
  - Set length: **one set, 14 songs, 54:46 in BandHelper** (51:31 of song time). Full list: `docs/setlist-az-state-fair.md`

## Decisions already made (don't re-litigate)

| Decision | Choice | Why |
|---|---|---|
| Stage DAW | **Ableton Live 12 Suite** (purchased) | Session View is built for looping sections; AbleSet; Max for Live. DP stays for writing and recording. |
| Show laptop | **Lenovo Yoga C940-15** (Windows). Editing happens on the **studio-pc** (MOTU 828es + analog rack). | Battery won't charge and it has crashed several times; see `docs/GEAR.md`. Use a UPS on stage. |
| Lighting software | **Obsidian ONYX** with the **NX DMX USB dongle** | More powerful and expandable than myDMX. |
| Lighting backup | **None.** myDMX is out (decided Sept 26, 2026) | ONYX only, including the State Fair. |
| Fixtures | **5 × Blizzard LB-Hex (RGBAW+UV) pars** | 11-channel mode (`CHNL` → `CH-2`), addresses 1/12/23/34/45. Verified against the LB-Hex manual Rev. C. |
| Setlists and lyrics | **BandHelper** on **Android tablets** | |
| Song selection | **AbleSet** in the tablet browser (first gig) | BandHelper → Ableton MIDI link comes after the first gig. |
| Drums | **Toontrack EZdrummer 3** with Acoustic Songwriter EZX and Latin Cuban Percussion EZX. Bought and installed on the studio-pc Sept 26, 2026; laptop still to install. | Same GM note map as the generated clips. |
| Bass | **Toontrack EZbass** for live shows and writing (laptop and studio-pc); **Spectrasonics Trilian** for production recording (studio-pc only). Decided Sept 26, 2026. | EZbass is light enough for the show laptop. Parts are MIDI, so they move to Trilian unchanged. |
| Lighting sync method | **MIDI notes per section**, not timecode | Timecode breaks when sections repeat or get skipped. |

## Two audio setups (decided Sept 26, 2026)

**The State Fair (Oct 4) uses the quick rig: MOTU M2, no click, lights on ONYX.** One Live set serves both. Switch the audio device in Preferences > Audio; the track routing below is what changes.

| | Quick rig | Full rig |
|---|---|---|
| Use | Busking, quick setups | Full shows |
| Interface | **MOTU M2** (2 outputs) | **Midas M32C + DL32 stage box** |
| Monitoring | No in-ears, no click | Multiple wireless in-ear mixes |
| Click | **None** | **Yes, in-ears only, never front of house** |
| Routing | Drums and bass summed to outputs 1/2 into the PA | Drums, bass and click on separate channels into the M32C so each in-ear mix gets its own balance |

Full-rig channel plan (proposed, confirm at the desk): Drums on 1/2, Bass on 3, Click on 4. The click comes from Live's metronome sent to the **Cue** output (Preferences > Audio > Cue Out = 4), so it never reaches the main outs. How the laptop connects to the M32C (its USB audio card, if fitted, or another route) still needs checking.

## How the rig fits together

```
BandHelper (Android tablets)       lyrics/chords
AbleSet (tablet browser, Wi-Fi) ──> Ableton Live 12 Suite (Windows)
Foot controller ─────────────────>   ├─ Drums track  (EZdrummer 3)
                                     ├─ Bass track   (EZbass)
                                     └─ Lights track ──> loopMIDI "Lights" ──> ONYX ──> NX DMX ──> 5 × LB-Hex
```

## What's in the repo

- `ableton/make_tracks.py`: dependency-free Python generator. Edit `SONGS` (tempo, feel, chords per bar per section) and run `python3 make_tracks.py`. It writes humanized drum, bass and lights MIDI into `ableton/clips/<song>/`.
  - Drums use the General MIDI drum note layout (kick 36, snare 38, hats 42/44/46, toms 43/45/47/50, crash 49, ride 51).
  - Bass stays between MIDI 40 (EZbass's open low E) and 51. EZbass uses 21-32 for keyswitches, so the General MIDI bass octave (28-39) fires slides and ghost notes instead of notes; that was the "distorted synth bass" on the first playback.
  - With a `form`, `make_set.py` makes one scene per form entry (Verse 1, Verse 2...) with a scene Follow Action: Next after the section's length, Stop on the last. Launching the first scene plays the song in order; clicking any scene jumps there and carries on from it. Follow action codes: No Action 0, Stop 1, Play Again 2, Previous 3, Next 4 (Next = 4 confirmed in Live 12.4.6).
  - `bass_variants` (per song, e.g. `["twofeel", "walkup", "pop8", "sparse"]`, styles in `BASS_STYLES`) writes `<section>-bass-<variant>.mid`. `make_set.py` gives each one a Bass track (`--update` copies the saved Bass track, EZbass sound included) and switches it off; the user A/Bs with the Track Activators while the song plays.
  - Per-song options: `form` (section order for the Full Song clip, which also gets a Lights clip), `verse_stick` (cross-stick backbeat in verse-style sections), and `"snare": True` on a section to keep full snare there.
  - After instruments are loaded and saved, refresh clips with `python make_set.py <song> "<saved .als>" --update`. It swaps clips, scenes and tempo and keeps the instruments and their sounds. Save in Live first, or unsaved sound changes are lost.
  - Every clip is an exact number of bars. Don't let notes run past the clip end, or Ableton adds an empty bar to the loop.
  - `LIGHT_CUES` maps sections to notes: intro 60, verse 62, prechorus 63, chorus 64, bridge 65, outro 67, fill 69, blackout 72.
- `ableton/make_set.py`: builds a Live Set (`.als`) for one song from its clips: Drums, Bass and Lights tracks, one scene per section (Full Song last), the song's tempo, every clip looping. Run `python make_set.py 02-halfway-gone "<path>.als"`. Instruments aren't written into the file; drop EZdrummer 3 and EZbass on, then Save As into the song's folder (Live makes a `<name> Project` folder).
  - Builds from `ableton/template.als`, an empty set saved by Live 12.4.6. Live's own `DefaultLiveSet.als` is an older 12.x file and comes up "corrupt (non-unique Pointee IDs)".
  - Copying a track means giving fresh IDs to every `*Target`, `Pointee` and `ControllerTargets.N` element, and to the track itself. Missing `ControllerTargets.N` was the cause of the corrupt-file warning.
  - Tempo lives in two places: `<Tempo><Manual>` and the main track's tempo automation event. Both get set.
- `ableton/clips/`: the four State Fair songs with tracks, numbered by setlist position: `02-halfway-gone` (104, A), `06-choosin-texas` (110, Db), `07-kiss-me` (100, Eb), `10-paper-stars` (88, Db). Chords are written in the sounding key (Dan, Sept 26: every other instrument plays in the natural key, so no capo shapes in the generator). Each song's `key` comment notes the guitar's shapes and capo for reference only. Bar counts are estimates from the lyric lines, to be fixed at rehearsal.
- `ableton/README.md`: 5-lesson Ableton guide for the user.
- `ableton/LIGHTING.md`: ONYX, loopMIDI and LB-Hex setup.
- `ableton/BANDHELPER.md`: Android MIDI options and AbleSet.
- `docs/GIG-PLAN.md`: countdown plan for the State Fair.
- `docs/RESEARCH.md`: research notes and sources.
- `docs/GEAR.md`: both computers, Toontrack libraries, guitar rig (DI-2, H90, Meraki), the three PA rigs, the studio rack, and the laptop's open hardware problems.

## Open tasks for the laptop session (in priority order)

The laptop has a Chrome connection; the cloud session that built this repo did not. Use the browser for these:

1. **Get the chord progression per section for each song.** Check BandHelper documents and lyrics first, then ask the user. Add each song to `SONGS` in `make_tracks.py` and regenerate the clips. Pick `feel` (straight/shuffle) and section `style` (light/verse/chorus/ending) per song. Ask the user when unsure.
2. Ask whether they want **AbleSet** now (Intro $129 / Standard $179 / Pro $269; free trial stops playback every 15 minutes). Standard is the sensible pick: two computers, OSC, redundancy.

### Done (Sept 26)

- AZ State Fair setlist pulled from BandHelper: `docs/setlist-az-state-fair.md`.
- Studio-pc: Toontrack libraries installed, Live 12.4.6 authorized, VST3 system folders on, audio on ASIO / MOTU Pro Audio (828es). Project folder on the T7 SSD (see `docs/GEAR.md`). Halfway Gone built with `make_set.py`, EZdrummer 3 and EZbass loaded, played back through the 828es.

- LB-Hex 11-channel layout and menu steps verified from the manual; written into `ableton/LIGHTING.md`. Channel 9 (built-in programs) must stay at 0.
- ONYX MIDI macro steps verified; written into `ableton/LIGHTING.md`. **A MIDIMACRO only listens after its cue has run**, so the show needs a "MIDI Listener" cue fired at startup.
- Band and Rylie websites reviewed; see `docs/RESEARCH.md`.

## Open questions for the user

- Foot controller: a **Morningstar** is planned (for the H90); none mapped in Ableton yet.
- AbleSet.
- Whether the DI-2 has a 1/4" output next to the XLR (decides the H90 wiring).

## Related

- An earlier copy of this work lives in `dpenn1000/DTech` under `band/ableton/` (PR #37, closed Sept 26, 2026, branch kept). This repo is the home for the band project.

## Writing style for anything the user reads

Plain, direct, conversational. Contractions. No em-dashes. Lead with the answer. Concrete numbers and names over adjectives. No filler intros or recap outros.
