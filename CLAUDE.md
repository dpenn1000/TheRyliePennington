# Daddy Long Legs: live rig project

Context for Claude sessions working in this repo. Read this first.

## Who and what

- **Daddy Long Legs** is a daddy-daughter acoustic duo: the dad (repo owner, dpenn1000) and his daughter **Rylie Pennington**. Websites: daddylonglegsband.com and ryliepennington.com.
- **Rylie** (13) sings and plays **guitar and bass guitar**, stars as the lead in the feature film *Not My Dog* (streaming since Sept 11, 2026; see `docs/RESEARCH.md`), has musical theatre credits, and sings the National Anthem at sporting events. The band writes originals and plays live gigs.
- **Consequence for the rig:** on songs where Rylie plays bass, the backing track should be drums only. Set `"bass": False` on that song in `make_tracks.py`. **As of Sept 26, 2026 nobody plays bass live, so every song gets a bass track.**
- The dad already uses **Digital Performer (DP)** for writing and recording and is new to Ableton.
- **Goal:** live drum and bass backing tracks that sound natural and follow the band. Sections loop until the band moves on, so a verse can be stretched and a bridge skipped on stage. Lighting follows the same section changes.
- **Next gig:** Arizona State Fair. The fair runs **Oct 1 to Nov 1, 2026, Thursday to Sunday**. The band plays the fair's first weekend, so `docs/GIG-PLAN.md`'s tight plan applies (3 to 5 songs with tracks, myDMX for lights, ONYX later).
  - Gig date: **Sunday, October 4, 2026, 1:00 to 2:00 pm**
  - Set length: **one set, 14 songs, 54:46 in BandHelper** (51:31 of song time). Full list: `docs/setlist-az-state-fair.md`

## Decisions already made (don't re-litigate)

| Decision | Choice | Why |
|---|---|---|
| Stage DAW | **Ableton Live 12 Suite** (purchased) | Session View is built for looping sections; AbleSet; Max for Live. DP stays for writing and recording. |
| Show laptop | **Windows PC** | |
| Lighting software | **Obsidian ONYX** with the **NX DMX USB dongle** | More powerful and expandable than myDMX. |
| Lighting backup | **ADJ myDMX dongle** | Kept for quick setups and as the on-stage fallback. |
| Fixtures | **5 × Blizzard LB-Hex (RGBAW+UV) pars** | 11-channel mode (`CHNL` → `CH-2`), addresses 1/12/23/34/45. Verified against the LB-Hex manual Rev. C. |
| Setlists and lyrics | **BandHelper** on **Android tablets** | |
| Song selection | **AbleSet** in the tablet browser (first gig) | BandHelper → Ableton MIDI link comes after the first gig. |
| Drums | Suite's **Session Drums Studio** now; **EZdrummer 3** recommended upgrade | |
| Bass | **Ample Bass P Lite** (free) now; **Toontrack EZbass** recommended upgrade | Suite's basses are mostly synth. |
| Lighting sync method | **MIDI notes per section**, not timecode | Timecode breaks when sections repeat or get skipped. |

## Two audio setups (decided Sept 26, 2026)

**The State Fair (Oct 4) uses the quick rig: MOTU M2, no click, lights on myDMX.** One Live set serves both. Switch the audio device in Preferences > Audio; the track routing below is what changes.

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
Foot controller ─────────────────>   ├─ Drums track  (Session Drums / EZdrummer)
                                     ├─ Bass track   (Ample Bass / EZbass)
                                     └─ Lights track ──> loopMIDI "Lights" ──> ONYX ──> NX DMX ──> 5 × LB-Hex
```

## What's in the repo

- `ableton/make_tracks.py`: dependency-free Python generator. Edit `SONGS` (tempo, feel, chords per bar per section) and run `python3 make_tracks.py`. It writes humanized drum, bass and lights MIDI into `ableton/clips/<song>/`.
  - Drums use the General MIDI drum note layout (kick 36, snare 38, hats 42/44/46, toms 43/45/47/50, crash 49, ride 51).
  - Bass stays between E1 (28) and D#2 (39).
  - Every clip is an exact number of bars. Don't let notes run past the clip end, or Ableton adds an empty bar to the loop.
  - `LIGHT_CUES` maps sections to notes: intro 60, verse 62, chorus 64, bridge 65, outro 67, fill 69, blackout 72.
- `ableton/clips/`: two **placeholder** songs (`01-front-porch` 96 BPM G straight, `02-campfire-shuffle` 84 BPM D shuffle). Replace them with the real setlist.
- `ableton/README.md`: 5-lesson Ableton guide for the user.
- `ableton/LIGHTING.md`: ONYX, loopMIDI and LB-Hex setup.
- `ableton/BANDHELPER.md`: Android MIDI options and AbleSet.
- `docs/GIG-PLAN.md`: countdown plan for the State Fair.
- `docs/RESEARCH.md`: research notes and sources.

## Open tasks for the laptop session (in priority order)

The laptop has a Chrome connection; the cloud session that built this repo did not. Use the browser for these:

1. **Pull the AZ State Fair setlist from BandHelper** (bandhelper.com web app: Repertoire > Set Lists; the Songs page has an Export button for account admins). For each song, capture title, tempo, key, time signature and duration. Save it as `docs/setlist-az-state-fair.md`.
2. **Get the chord progression per section for each song.** Check BandHelper documents and lyrics first, then ask the user. Add each song to `SONGS` in `make_tracks.py` and regenerate the clips. Pick `feel` (straight/shuffle) and section `style` (light/verse/chorus/ending) per song. Ask the user when unsure.
3. Ask whether they want **AbleSet** now (Intro $129 / Standard $179 / Pro $269; free trial stops playback every 15 minutes). Standard is the sensible pick: two computers, OSC, redundancy.

### Done (Sept 26, cloud session)

- LB-Hex 11-channel layout and menu steps verified from the manual; written into `ableton/LIGHTING.md`. Channel 9 (built-in programs) must stay at 0.
- ONYX MIDI macro steps verified; written into `ableton/LIGHTING.md`. **A MIDIMACRO only listens after its cue has run**, so the show needs a "MIDI Listener" cue fired at startup.
- Band and Rylie websites reviewed; see `docs/RESEARCH.md`.

## Open questions for the user

- Which foot controller they own, if any.
- Whether they've bought EZdrummer 3, EZbass or AbleSet.

## Related

- An earlier copy of this work lives in `dpenn1000/DTech` under `band/ableton/` (PR #37, closed Sept 26, 2026, branch kept). This repo is the home for the band project.

## Writing style for anything the user reads

Plain, direct, conversational. Contractions. No em-dashes. Lead with the answer. Concrete numbers and names over adjectives. No filler intros or recap outros.
