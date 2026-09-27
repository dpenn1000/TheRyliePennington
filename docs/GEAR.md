# Gear

Everything the band owns or plans to buy, and how it's wired. Decided Sept 26, 2026 unless noted.

## Two computers

| | Show laptop | studio-pc |
|---|---|---|
| Machine | Lenovo Yoga C940-15 (type 81TE), i7-9750H, 16 GB, GTX 1650 Max-Q, 512 GB Intel H10 SSD | Studio desktop |
| Job | Plays the show: Ableton, ONYX, loopMIDI | Writing, recording, editing |
| Interface | MOTU M2 (quick rig) | MOTU 828es, 48 kHz, internal clock |
| Drums | EZdrummer 3 | Superior Drummer 3 Orchestral Edition (later) |
| Bass | EZbass | Trilian (later), and Rylie playing for real |

**Shared files:** Live Sets and ONYX shows sync through OneDrive (`Music\Daddy Long Legs\`). Never open the same set on both machines at once. Use File > Collect All and Save. Sample libraries install on each machine separately, never in OneDrive. On the laptop, mark the show folder "Always keep on this device" and pause OneDrive during shows. Keep a gig copy on an external SSD (exFAT).

**This repo** is cloned on each machine (laptop: `C:\Shows\DaddyLongLegs`), not in OneDrive.

### Show laptop problems (open)

- **Battery won't charge.** Four batteries this year. The current one is aftermarket and reports 111% of design capacity, 0% charge, not charging. The laptop dies the instant it's unplugged. A genuine Lenovo 135 W charger is on order; the current brick may be non-Lenovo. Next test: genuine charger, then BIOS "Disable Built-in Battery" reset, then a genuine battery. **Use a UPS on stage.**
- **Freezes and crashes.** Bugcheck 0x154 (Aug 3, 4, 8, Sept 26), 0x1E (Sept 17), hard freezes Sept 20 and 26. Fixes in progress: MOTU M2 driver 4.6.0.705 (installed Sept 26), NVIDIA Studio driver (was 457.49 from 2020), Lenovo System Update, memory test (`mdsched`). If it keeps happening, suspect hardware.
- `laptop/gig-mode-on.ps1` / `laptop/gig-mode-off.ps1` (run in an admin PowerShell) close background apps and switch to a no-throttle power plan for shows.

## Toontrack shopping list

1. **EZdrummer 3** bundle + **Acoustic Songwriter EZX** (7 Nashville-recorded kits for songwriter, country, folk, pop)
2. **EZbass Bundle** ($269) with **Upright EBX** and **Session Player EBX** ('63 P-bass, flatwounds, recorded through a flip-top amp). Core EZbass adds a vintage Jazz and a modern Alembic.
3. **Latin Cuban Percussion EZX** (congas, bongos, timbales, cajón, shakers; MIDI by Richie Flores). Confirm EZdrummer 3 compatibility with Toontrack first.
4. Later: The Eighties EBX (Wal + Minimoog), Session Legend EBX (BB3000), Americana EBX (Tele bass), Singer-Songwriter EZX.

EZbass for live and writing; Trilian for production. Parts are MIDI, so they move between the two unchanged. For Rylie's originals, she plays the real bass part in the studio.

## Guitar rig (dad, acoustic)

```
Guitar ─> Sunnaudio Stage DI-2 ─┬─ XLR ─────────────────────────> Mixer: DRY (all analog)
                                └─ 1/4" ─> Eventide H90 (Kill Dry) ─> Mixer: effects only
Morningstar controller ─MIDI─> H90, one program per song
Expression pedal ─> H90: heel = drier, toe = more reverb and chorus (same job in every program)
```

- **Stage DI-2 Prestine:** all-analog preamp, EQ, HPF, boost and mute switches, effects insert. Keep.
- **Eventide H90:** replaces the H9. Runs two effects at once (chorus into reverb). About 3.8 ms parallel / 4.5 ms series. In parallel with Kill Dry, the dry tone never goes digital.
- **Walrus Meraki:** true analog stereo delay (8 × MN3005). Keep for its warmth, in the DI-2 insert (mono), or run it in stereo after the DI-2's 1/4" out on a stereo PA.
- **Retire:** Eventide H9 (sell toward the H90), Fender Smolder (rarely used), Boss bass pedal (once more songs have backing tracks).
- Check whether the DI-2 has a 1/4" out next to the XLR. If not, the H90 goes in the insert and the dry signal passes through it.
- Later: Ableton can send H90 program changes per song or section from a MIDI track, like the Lights track.

## PA rigs

| Rig | Gear | Use |
|---|---|---|
| Busking / no power | **Elite Acoustics D6-58**: 120 W, 8" + 5.25" + 1", 6-channel digital mixer, 48 V on 4 mic inputs, LiFePO4 battery (4 to 6 h) | Street, patio, markets. Turn off its reverb and chorus on the guitar channel. The laptop still needs wall power. |
| Small / indoor | Pair of **RCF HD 10-A MK5**: 800 W, 10" + 1", 128 dB max, 90 × 60°, FiRPHASE | Restaurants, private events |
| Large / outdoor | Pair of **EAW RS123** (12" two-way, 1500 W, EAW Focusing + DynO, 90 × 60°) over one **EAW RS118** 18" sub | State Fair, festivals |

EAW tips: pole-mount the tops on the sub, use EAW's matched sub and top presets, skip heavy EQ at the mixer (the speakers are already phase-correct), and set backing tracks about 12 dB under the vocals to start.

## Studio rack (studio-pc)

| Unit | Use |
|---|---|
| MOTU 828es | Interface, 48 kHz internal clock |
| Sebatron vmp-4000e (4-ch tube pre, DI inputs, air/bright, deep/lo-cut) | Rylie's lead vocal with air on |
| TK Audio DP2 (2-ch pre, Hi-Z, HPF, color modes) | Rylie's bass DI |
| Buzz Audio MA-2.2 (2-ch true Class A pre) | Stereo acoustic guitar; clean modern vocal |
| IGS Zen (stereo Zener-diode compressor/limiter, EMI TG12413 style, solid state; comp and limit modes, sidechain HPF) | Fast, smooth, musical control on stereo acoustic or vocals; also a bus compressor |
| AudioScape AS78 (dual peak limiter, 1176-style) | Vocal peaks, 2 to 4 dB |
| SSL Fusion (stereo analog color) | Mix bus color |
| IGS Tubecore Mastering Edition (stereo vari-mu, M/S, mix) | Mix bus glue, last in chain |

Starting chains:
- Vocal: Pearlman TM-1 → Buzz MA-2.2 or Sebatron (A/B by ear) → AS78 → 828es
- Acoustic: stereo pair → Buzz MA-2.2 → IGS Zen (linked) → 828es
- Bass: DI → TK DP2 (Hi-Z) → 828es
- Mix bus (hardware inserts from DP): SSL Fusion → IGS Tubecore

## Rylie's vocal mics

| Where | Mic | Notes |
|---|---|---|
| Studio | **Pearlman TM-1** (tube condenser) | Her favorite so far. Try it into the Buzz MA-2.2 (clean) first, then the Sebatron (tube on tube, warmer). Pick by ear. |
| Live | **Beyerdynamic M88** (dynamic, hypercardioid) | Warm, natural tone. Hypercardioid: its least sensitive spot is about 110° to 120° off-axis, not straight behind, so angle wedges accordingly or run in-ears. Strong proximity effect: use a high-pass around 80 to 100 Hz and coach a consistent distance. |

Other studio mics: not yet listed.

## Lights

ONYX only, with the Obsidian NX DMX dongle and 5 Blizzard LB-Hex pars. myDMX is out. loopMIDI port `Lights` installed on the laptop Sept 26. See `ableton/LIGHTING.md`.
