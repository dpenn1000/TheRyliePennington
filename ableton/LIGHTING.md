# Lighting: Ableton → ONYX → 5 Blizzard LB-Hex pars

Every section clip in Ableton has a matching `Lights` clip. When a scene launches, the Lights clip sends one MIDI note, and ONYX fires the look for that section. Stretch the verse and the verse look stays. Jump to the chorus and the chorus look lands on the same downbeat as the drums.

```
Ableton (Lights track) ──MIDI──> loopMIDI (virtual cable) ──> ONYX ──USB──> NX DMX dongle ──DMX──> 5 × LB-Hex
```

Everything runs on the one Windows laptop.

## The note chart

| Section | Note (Ableton name) | MIDI # | Suggested look |
|---|---|---|---|
| Intro | C3 | 60 | Warm amber, 40% |
| Verse | D3 | 62 | Warm wash, 60% |
| Chorus | E3 | 64 | Full, brighter color, 100% |
| Bridge | F3 | 65 | Cool blue/UV, 50% |
| Outro | G3 | 67 | Build to full, hold |
| Fill | A3 | 69 | Quick white bump |
| Blackout | C4 | 72 | All off |

This table lives in `make_tracks.py` as `LIGHT_CUES`. Change it there and re-run to regenerate every Lights clip.

Heads-up: some programs call note 60 "C4" instead of "C3". If ONYX shows a note one octave off from this chart, it's the same note with a different label. Trust the MIDI number.

## Step 1: Address the pars

The LB-Hex has **6-channel** and **11-channel** DMX modes. Use **11-channel**: it adds a master dimmer and strobe, which ONYX needs for smooth fades.

On each fixture (buttons: MENU, UP, DOWN, ENTER):

1. Scroll to **`CHNL`**, press ENTER, choose **`CH-2`** (11-channel), ENTER.
2. Scroll to **`Addr`**, press ENTER, set the address from the table, ENTER.

| Par | Address | Position |
|---|---|---|
| 1 | 001 | Far stage left |
| 2 | 012 | Stage left |
| 3 | 023 | Center (backlight) |
| 4 | 034 | Stage right |
| 5 | 045 | Far stage right |

The NX DMX has two 5-pin XLR ports; use port 1 (Universe 1). If the pars' DMX jacks are 3-pin, you need a 5-pin to 3-pin adapter or cable. Check before gig day.

Chain them with DMX cables: dongle → par 1 → par 2 → … → par 5. Put a DMX terminator in the last one if you have one (it stops flicker on long runs).

### 11-channel layout (from the LB-Hex manual, Rev. C)

| Ch | Function |
|---|---|
| 1 | Dimmer (master) |
| 2 | Red |
| 3 | Green |
| 4 | Blue |
| 5 | Amber |
| 6 | White |
| 7 | UV |
| 8 | Strobe (slow → fast; 0 = off) |
| 9 | Built-in programs / auto / sound active. **Keep at 0 for ONYX control.** |
| 10 | Program speed |
| 11 | Dimming curve |

If a par ignores ONYX or runs its own color chase, channel 9 isn't at 0, or the fixture is stuck in a standalone mode (`Pr--`, `SOUN`). Reset to DMX by setting the address again.

## Step 2: Wire Ableton to ONYX (same PC)

Windows can't pass MIDI between two programs by itself. A free virtual cable fixes that.

1. Install **loopMIDI** (free, by Tobias Erichsen). Open it and click **+** to create a port. Name it `Lights`.
2. **Ableton:** Options > Preferences > Link, Tempo & MIDI. Find `Lights` under **Output** and turn **Track** on.
3. On the Ableton `Lights` track: set **MIDI To** to `Lights`, channel 1.
4. **ONYX:** in its settings, enable `Lights` as a MIDI input. Use ONYX's MIDI-In event viewer to confirm notes arrive when you launch a scene in Ableton.

## Step 3: Build the looks in ONYX

1. Patch 5 × **Blizzard LB-Hex, 11-channel** at the addresses above. Search "Blizzard" in the fixture library. If it's missing, build a generic fixture from the channel table above.
2. Make one cuelist per section look: Intro, Verse, Chorus, Bridge, Outro, Fill, Blackout.
3. Make a separate cuelist called **`MIDI Listener`** with one cue. In that cue, add one MIDI macro per look:
   - **Add Macro** → type **`MIDIMACRO`**. The **MIDI In Event Viewer** opens.
   - Pick the target cuelist (e.g. Verse) and the action **Go**.
   - MIDI command **Note-On**, channel 1, **Data 1** from/to = the note number from the chart (e.g. 62–62), **Data 2** from/to = 1–127.
   - Shortcut: launch the matching scene in Ableton, then click the note when it shows up in the Event Viewer. That fills the fields in for you.
   - Press **Apply**. Repeat for all seven looks.
4. **The catch:** a MIDI macro only listens after the cue it lives in has been run. At the start of every show (and after reopening ONYX), **run the MIDI Listener cue once**. Put it on a button you can't miss, or the lights will ignore Ableton all night.
5. Give each look cue a **2-second fade** so looks glide instead of snapping. Give Fill a **0** fade in and a short release.

## Step 4: Load the Lights clips in Ableton

Drag each `*-lights.mid` file into the `Lights` track in the same row as its drums and bass. Then, for each Lights clip, open it (double-click) and **turn Loop off**. The note should fire once when the section starts, not again every time the clip loops.

## The MyDMX backup

Keep the MyDMX dongle in the gig bag. If the laptop or ONYX has a problem, unplug the NX dongle, plug in MyDMX with a saved sound-active scene, and the show still has lights.

## Resources

- [LB-Par Hex manual (DMX chart)](https://www.fullcompass.com/common/files/39583-LBPARHEXUserManual.pdf)
- [ONYX: Setting Cue Triggers](https://support.obsidiancontrol.com/Content/Onyx_Manual/Playback/Cues_and_Cuelists/Cue_Timing/Setting_Cue_Triggers.htm)
- [ONYX: MIDI Macros](https://support.obsidiancontrol.com/Content/Onyx_Manual/Playback/Cues_and_Cuelists/Modifying_Cues/Cue_Macros/Midi_Macros.htm)
