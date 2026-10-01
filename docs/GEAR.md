# Gear

Everything the band owns or plans to buy, and how it's wired. Decided Sept 26, 2026 unless noted.

## Two computers

| | Show laptop | studio-pc |
|---|---|---|
| Machine | Lenovo Yoga C940-15 (type 81TE), i7-9750H, 16 GB, GTX 1650 Max-Q, 512 GB Intel H10 SSD | Studio desktop |
| Job | Plays the show: Ableton, ONYX, loopMIDI | Writing, recording, editing |
| Interface | MOTU M2 (quick rig) | MOTU 828es, 48 kHz, internal clock |
| Live | Ableton Live 12 Suite | Ableton Live 12 Suite 12.4.6, ASIO on MOTU Pro Audio, VST3 system folders on |
| Drums | EZdrummer 3 (to install) | EZdrummer 3 + Acoustic Songwriter EZX + Latin Cuban Percussion EZX (installed); Superior Drummer 3 Orchestral Edition (later) |
| Bass | EZbass (to install) | EZbass + Upright EBX + Session Player EBX (installed); Trilian is a possible future upgrade, not owned (corrected 2026-09-27), and Rylie playing for real |

**Shared files:** the project lives on the **Samsung T7 SSD** (exFAT, `E:` on the studio-pc) in `Daddy Long Legs\`, and moves between machines on the drive. The drive letter may differ on the laptop; Live finds files relative to each project folder. Use File > Collect All and Save before unplugging. Sample libraries install on each machine separately, never on the T7 or in OneDrive. Charts, marketing, photos and video stay in OneDrive (`Music\Daddy Long Legs\`).

```
Daddy Long Legs\
  Songs\<song>\                     one folder per song, named by title (no setlist number)
    <name> Project\                 the song's Live Set (Live creates this on first save)
    MIDI\                           clips from make_tracks.py
    Audio\Reference, Recordings, Bounces
  Shows\2026-10-04 AZ State Fair\   the show set that strings the songs together
  Lighting\ONYX Shows, Fixtures
  Audio\Samples, Loops              shared across songs
  Recordings\Studio, Live           full sessions and gig recordings
  Exports\Backing Tracks, Mixes
  Templates\  Backups\
```

**This repo** is cloned on each machine (laptop: `C:\Shows\DaddyLongLegs`), not in OneDrive.

### Show laptop problems (open)

- **Battery won't charge.** Four batteries this year. The current one is aftermarket and reports 111% of design capacity, 0% charge, not charging. The laptop dies the instant it's unplugged. A genuine Lenovo 135 W charger is on order; the current brick may be non-Lenovo. Next test: genuine charger, then BIOS "Disable Built-in Battery" reset, then a genuine battery. **Use a UPS on stage.**
- **Freezes and crashes.** Bugcheck 0x154 (Aug 3, 4, 8, Sept 26), 0x1E (Sept 17), 0xEF during Modern Standby (Sept 27, 5:43 am, after an hour of the Intel Wi-Fi card waking every 2 minutes), hard freezes Sept 20 and 26. **Likely cause: devices (the Intel H10 SSD, the Wi-Fi card) failing to come back from low-power states.** Memory test passed Sept 26.
  - Done Sept 26 to 27: MOTU M2 driver 4.6.0.705, NVIDIA driver 32.0.16.1714 (Sept 2026), Lenovo System Update (nothing newer), Smart Performance auto-scans off, and on AC power: never sleep, drive never powers down, PCIe link power saving off, no network in standby.
  - Next if it crashes again: newer Intel Wi-Fi driver, then Intel's current UHD 630 graphics driver (Lenovo's is from Feb 2020; make a restore point first).
- `laptop/gig-mode-on.ps1` / `laptop/gig-mode-off.ps1` (run in an admin PowerShell) close background apps and switch to a no-throttle power plan for shows.

## Toontrack

Bought and installed on the studio-pc Sept 26, 2026 (installer log: every package succeeded). The laptop still needs them. Drum libraries take 34 GB, bass 4.5 GB.

| Product | Studio-pc | Laptop |
|---|---|---|
| **EZdrummer 3** 3.1.2 + Core Library (Main, Bright and Tight rooms) | Installed | To install |
| **Acoustic Songwriter EZX** (7 Nashville-recorded kits for songwriter, country, folk, pop) | Installed | To install |
| **Latin Cuban Percussion EZX** (congas, bongos, timbales, cajón, shakers; MIDI by Richie Flores) | Installed | To install |
| **EZbass** 1.1.2 + Core Library (vintage Jazz, modern Alembic) | Installed | To install |
| **Upright EBX** | Installed | To install |
| **Session Player EBX** ('63 P-bass, flatwounds, recorded through a flip-top amp) | Installed | To install |

Later: The Eighties EBX (Wal + Minimoog), Session Legend EBX (BB3000), Americana EBX (Tele bass), Singer-Songwriter EZX.

EZbass for live, writing, and production; it's not owned yet, but if Trilian gets bought later, parts are MIDI, so they'd move over unchanged. For Rylie's originals, she plays the real bass part in the studio.

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
- Acoustic: AEA R84 at the body + Lewitt LCT 440 PURE at the 12th fret → Buzz MA-2.2 → IGS Zen (linked) → 828es. Stereo option: Royer R-10 pair as Blumlein.
- Bass: DI → TK DP2 (Hi-Z) → 828es
- Mix bus (hardware inserts from DP): SSL Fusion → IGS Tubecore

## Rylie's vocal mics

| Where | Mic | Notes |
|---|---|---|
| Studio | **Pearlman TM-1** (tube condenser) | Her favorite so far. Try it into the Buzz MA-2.2 (clean) first, then the Sebatron (tube on tube, warmer). Pick by ear. |
| Live | **Beyerdynamic M88** (dynamic, hypercardioid) | Warm, natural tone. Hypercardioid: its least sensitive spot is about 110° to 120° off-axis, not straight behind, so angle wedges accordingly or run in-ears. Strong proximity effect: use a high-pass around 80 to 100 Hz and coach a consistent distance. |

### Mic locker

| Mic | Type | Best use here |
|---|---|---|
| Pearlman TM-1 | Tube condenser | **Rylie's lead vocal.** Sits her right in the mix every time. The default, not up for debate |
| Lauten Audio Atlantis | Large-diaphragm FET condenser, multi-pattern, G/N/F voicing modes | **Dad's vocal** (loves it on his voice). Not for Rylie: its sibilance lands wrong on her voice. Also acoustic guitar |
| AEA R84 | Large ribbon, figure-8 | Acoustic guitar (body), smooth vocal alternative, room |
| Royer R-10 (pair) | Ribbon, figure-8 | Stereo acoustic guitar or room (Blumlein), percussion |
| Lewitt LCT 440 PURE | Large-diaphragm condenser, cardioid | Acoustic guitar (12th fret), dad's vocal, clean utility mic |
| Beyerdynamic TG V90r | Ribbon, **cardioid**, handheld stage vocal mic; survives accidental phantom; 50 Hz to 14 kHz | Warm live vocals for either singer; smooth studio vocal alternative |
| Beyerdynamic M 201 TG (×2) | Dynamic, hypercardioid. Dad's take: an SM57 but better and far more focused | Percussion, guitar cabs, loud sources; second cajón mic; tight pickup on a busy stage |
| Telefunken M80 (several) | Dynamic, supercardioid | Dad's live vocal, backups for Rylie live |
| Telefunken M82 | Large-diaphragm dynamic (kick mic), switchable kick EQ and high boost | **Cajón** (dad's pick): inside or at the back port for the low thump |
| Beyerdynamic M88 | Dynamic, hypercardioid | Rylie's live vocal |
| Neumann KMS 105 (×2) | Handheld condenser, supercardioid (needs phantom) | Detailed, studio-like live vocals for either singer; A/B against the M88 on the RCF or EAW rigs |

**Ribbons (R84, R-10):** keep phantom power off on their channels as a habit, and give them a preamp with lots of clean gain (Buzz MA-2.2 first). Figure-8 means they pick up equally from the back, so aim the back at something you don't mind hearing.

## Lights

ONYX only, with the Obsidian NX DMX dongle and 5 Blizzard LB Hex Unplugged (battery) pars. myDMX is out. loopMIDI port `Lights` installed on the laptop Sept 26. See `ableton/LIGHTING.md`.

## Valuation

Line-item cost and resale basis for the gear above, for insurance and tax records. Full detail (MSRP, street price, source URLs, per-item notes) lives in `studio_gear_valuation.xlsx` in this folder; this table is the purchased-cost and used-resale-estimate summary, sorted by purchase price.

| Item | Qty | Owned | Purchased ($) | Used Est. ($) |
|---|---|---|---|---|
| Schoeps Stereo Set MK 22 (CMC622ST Open Cardioid) | 1 | 1 year | 2,802.83 | 2,200.00 |
| IGS Audio Tubecore 3U Vari-mu Compressor (assumed rack version) | 1 | 2 years | 2,777.54 | 1,900.00 |
| RDY North 003 Computer (model/specs unspecified) | 1 | 1 year | 2,034.41 | 750.00 |
| Guild F-50 Jumbo Acoustic Guitar | 1 | 2 years | 1,845.18 | 1,300.00 |
| IGS Audio ZEN Stereo Mastering Compressor | 1 | <1 year | 1,700.00 | 1,350.00 |
| RCF ART 710-A MK5 10" Powered Speaker | 4 | 2 years | 1,659.08 | 1,200.00 |
| ASUS ProArt Monitor(s) (model unspecified) | 1 | <1 year | 1,614.34 | 1,200.00 |
| Sennheiser ew IEM G4-TWIN (wireless in-ear monitoring system) | 1 | <1 year | 1,564.36 | 1,200.00 |
| GIK Acoustics Treatment (panels/bass traps; details unspecified) | 1 | 2 years | 1,417.00 | 500.00 |
| Handcrafted Labs Thermos Equalizer (Mastering EQ) | 1 | 1 year | 1,329.38 | 900.00 |
| AudioScape AS78 Dual FET Peak Limiter (1178-style) | 1 | <1 year | 1,289.00 | 1,100.00 |
| Sebatron VMP-4000 (4-channel tube preamp) (model variant unspecified) | 1 | 2 years | 1,223.03 | 700.00 |
| Pearlman TM-1 Tube Condenser Microphone (German tube) | 1 | <1 year | 1,201.76 | 900.00 |
| Grace Design ROXi Mic/Instrument Preamp Pedal | 1 | 2 years | 951.83 | 550.00 |
| Radial Microphone Splitter (assumed JS3) | 2 | 2 years | 940.00 | 700.00 |
| Lauten Audio Atlantis FC-387 Microphone | 1 | 2 years | 933.19 | 500.00 |
| TK Audio DP2 Dual Class-A Preamp | 1 | 1 year | 893.34 | 550.00 |
| Elite Acoustics D6-58 Acoustic Amp | 1 | 1 year | 824.21 | 550.00 |
| Waves 'ERC1' Advanced WiFi Router (model unspecified) | 1 | 2 years | 637.00 | 250.00 |
| Roc-N-Soc Thrones/Chairs (model/config unspecified), assumed 2 units | 2 | <1 year | 595.56 | 400.00 |
| Eventide H9 Max Multi-effects Pedal | 1 | 2 years | 558.24 | 350.00 |
| Sennheiser ew 100 G4-CI1 Wireless Instrument Set (band unspecified) | 1 | 1 year | 549.99 | 300.00 |
| Beyerdynamic M 201 Hypercardioid Dynamic Instrument Mic | 2 | 3 years | 457.30 | 250.00 |
| Strymon BigSky Multidimensional Reverb Pedal | 1 | 1 year | 372.23 | 250.00 |
| Beyerdynamic TG V90r Ribbon Microphone | 1 | 2 years | 372.23 | 200.00 |
| Saaria Velvet Curtain (acoustic treatment) (details unspecified) | 1 | 1 year | 344.00 | 180.00 |
| Beyerdynamic Microphone (model unspecified) | 1 | 2 years | 339.26 | 150.00 |
| Telefunken M80 Dynamic Microphone (Black) | 2 | 2 years | 300.00 | 220.00 |
| White Oak Audio Rack (custom / furniture) | 1 | <1 year | 280.00 | 170.00 |
| Bass Guitar (model unspecified) | 1 | <1 year | 236.09 | 120.00 |
| DI Boxes (Radial/Telefunken), model unspecified | 3 | 2 years | 148.00 | 70.00 |
| Gator Frameworks GFW-MICSTDBAG (carry bag for up to 6 tripod mic stands) | 1 | 3 years | 124.99 | 70.00 |
| Telefunken 'TDA-1DL' (model unclear), assumed small accessory/DI | 2 | 3 years | 119.94 | 40.00 |
| Aureday 64" Phone&Tablet Tripod w/ remote (iPhone/iPad holder), consolidated | 2 | <1 year | 65.98 | 20.00 |
| Kate Collapsible Pop-Up Backdrop (self-tape / headshots / streaming) | 1 | <1 year | 45.99 | 20.00 |

| Totals | |
|---|---|
| Total purchased (cost basis) | $32,547.28 |
| Total MSRP/list | $37,204.52 |
| Total new street | $35,494.72 |
| Total estimated used resale | $21,110.00 |
| Recovery vs. purchased | 65% |
| Recovery vs. new street | 59% |
| Items still missing MSRP/street or model confirmation | 10, flagged in the xlsx's `Missing MSRP/Street?` column |
