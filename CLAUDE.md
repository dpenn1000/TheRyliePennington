# Daddy Long Legs: live rig project

Context for Claude sessions working in this repo. Read this first.

## Who and what

- **Daddy Long Legs** is a daddy-daughter acoustic duo: the dad (repo owner, dpenn1000) and his daughter **Rylie Pennington**. Websites: daddylonglegsband.com and ryliepennington.com.
- **Rylie** sings and plays **guitar and bass guitar**, has musical theatre and film credits, and sings the National Anthem at sporting events. The band writes originals and plays live gigs.
- **Consequence for the rig:** on songs where Rylie plays bass, the backing track should be drums only. Set `"bass": False` on that song in `make_tracks.py`. Ask the user which songs those are.
- The dad already uses **Digital Performer (DP)** for writing and recording and is new to Ableton.
- **Goal:** live drum and bass backing tracks that sound natural and follow the band. Sections loop until the band moves on, so a verse can be stretched and a bridge skipped on stage. Lighting follows the same section changes.
- **Next gig:** Arizona State Fair. The fair runs **Oct 1 to Nov 1, 2026, Thursday to Sunday**. The band's exact date and time slot are not yet recorded here. **Ask the user and write it below.**
  - Gig date: _TBD_
  - Set length: _TBD_

## Decisions already made (don't re-litigate)

| Decision | Choice | Why |
|---|---|---|
| Stage DAW | **Ableton Live 12 Suite** (purchased) | Session View is built for looping sections; AbleSet; Max for Live. DP stays for writing and recording. |
| Show laptop | **Windows PC** | |
| Lighting software | **Obsidian ONYX** with the **NX DMX USB dongle** | More powerful and expandable than myDMX. |
| Lighting backup | **ADJ myDMX dongle** | Kept for quick setups and as the on-stage fallback. |
| Fixtures | **5 × Blizzard LB-Hex (RGBAW+UV) pars** | Plan: 11-channel mode, addresses 1/12/23/34/45 (verify, see tasks). |
| Setlists and lyrics | **BandHelper** on **Android tablets** | |
| Song selection | **AbleSet** in the tablet browser (first gig) | BandHelper → Ableton MIDI link comes after the first gig. |
| Drums | Suite's **Session Drums Studio** now; **EZdrummer 3** recommended upgrade | |
| Bass | **Ample Bass P Lite** (free) now; **Toontrack EZbass** recommended upgrade | Suite's basses are mostly synth. |
| Lighting sync method | **MIDI notes per section**, not timecode | Timecode breaks when sections repeat or get skipped. |

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
3. **Verify the LB-Hex DMX modes.** The plan assumes 6- or 11-channel modes; confirm from the Blizzard manual (blizzardpro.com product page or the manual PDF), including whether the user's units are the battery "Unplugged" model. Record the 11-channel layout in `ableton/LIGHTING.md`.
4. **Verify the ONYX MIDI trigger steps** in the ONYX manual (support.obsidiancontrol.com: "Midi Macros", "Cuelist Options", "Function Assignments"). Search results indicate a MIDI "Note On" macro with Channel / Data 1 (note) / Data 2 (velocity) that runs Go on a cuelist. Replace the general wording in `ableton/LIGHTING.md` with exact menu paths.
5. **Look at daddylonglegsband.com and ryliepennington.com** for the band's style, originals vs covers, and any song list; note it in `docs/RESEARCH.md`. Don't copy personal or health details about Rylie into this repo; it's public.
6. Check the exact **AbleSet** edition and price (ableset.com) and whether the user has bought it.

## Open questions for the user

- Exact State Fair date, time slot and set length.
- Which foot controller they own, if any.
- Audio interface model on the Windows laptop, and whether they want the click in their ears only (needs 4 outputs).
- Whether they've bought EZdrummer 3, EZbass or AbleSet.
- Which songs Rylie plays bass on (drums-only backing for those), and who plays what on the rest.
- Monitoring: in-ear vs wedge, and whether a click is wanted at all. Check with the user before designing monitor mixes.

## Related

- An earlier copy of this work lives in `dpenn1000/DTech` under `band/ableton/` (draft PR #37). This repo is now the home for the band project.

## Writing style for anything the user reads

Plain, direct, conversational. Contractions. No em-dashes. Lead with the answer. Concrete numbers and names over adjectives. No filler intros or recap outros.
