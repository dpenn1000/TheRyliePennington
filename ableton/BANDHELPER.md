# BandHelper on Android → Ableton

Goal: pick a song on the tablet, and the lyrics come up, Ableton jumps to that song, and the lights follow.

## For the State Fair: keep it simple

Wiring BandHelper to Ableton adds another cable, another setting and another thing to debug on stage. For the first gig:

- **BandHelper** on the tablets: lyrics and chords only.
- **AbleSet** for song selection. It runs in a web browser, so the Android tablets work. Tablets and laptop join the same Wi-Fi (bring your own travel router; fair Wi-Fi won't hold up), and anyone can tap the next song.
- Scenes launch from the foot pedal.

Add the BandHelper-to-Ableton link once the basic show runs clean.

## Wiring BandHelper to Ableton (after the first gig)

BandHelper on Android 6 or later can send MIDI over **USB** (with a USB-OTG cable) or **Bluetooth**.

**Option A: wired (most reliable).** Tablet → USB-OTG cable → a USB MIDI host interface → the laptop. The tablet and the PC both expect to be the "boss" of a USB connection, so a plain cable between them won't work. You need a small MIDI interface in the middle that has host ports for both. Tell me what you already own before buying one.

**Option B: Wi-Fi.** BandHelper's older MIDI framework (Help > Utilities > Use Old MIDI Framework) can send network MIDI (RTP). On the PC, install **rtpMIDI** (free, by Tobias Erichsen) to receive it. This rides on the same travel router as AbleSet. I haven't confirmed this still works on current Android versions, so test it at home first.

### Mapping

1. In BandHelper, give each song a MIDI preset that sends one **Program Change** (Song 1 = PC 1, Song 2 = PC 2, …).
2. In AbleSet's MIDI mapping, map each Program Change to "jump to song." AbleSet then takes Ableton to that song's first scene.
3. Tap a song in BandHelper. Check that Ableton moves, then check that the lights change on the first scene launch.

## Resources

- [BandHelper: Sending MIDI](https://www.bandhelper.com/tutorials/sending_MIDI.html)
- [BandHelper: Hardware](https://www.bandhelper.com/support/hardware.html)
- [AbleSet: MIDI mapping](https://ableset.app/docs/midi-mapping/)
