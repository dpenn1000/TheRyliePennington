# Ableton backing tracks: Daddy Long Legs

Drum and bass backing for a live duo, built so the band steers the song instead of chasing a recording. Each song is split into sections (intro, verse, chorus, bridge, outro). Each section loops until you tell it to move on. Stretch a verse when the crowd's singing along, cut a chorus short when the kid needs a break.

## What's in here

```
clips/
  02-halfway-gone/       104 BPM, key of A   (G shapes, capo 2)
  06-choosin-texas/      110 BPM, key of Db  (C shapes, capo 1)
  07-kiss-me/            100 BPM, key of Eb  (D shapes, capo 1)
  10-paper-stars/         88 BPM, key of Db  (C shapes, capo 1)
    0-full-song-*.mid    whole song start to finish (for Arrangement View)
    1-intro-*.mid        light: sidestick, pedal hat, whole-note bass
    2-verse-*.mid        hats, backbeat, ghost notes, root-fifth bass
    3-prechorus-*.mid    (Halfway Gone and Paper Stars only)
    *-chorus-*.mid       crash on the one, driving 8th-note bass
    *-bridge-*.mid       drops back to light (the solo, in Kiss Me)
    *-outro-*.mid        big ending, last hit rings
    *-fill-drums.mid     one bar with a fill, for launching by hand
    *-lights.mid         one MIDI note per section, fires the ONYX look
LIGHTING.md              Ableton → ONYX → Blizzard LB-Hex setup
BANDHELPER.md            BandHelper (Android) + AbleSet setup
make_tracks.py           the generator; edit chords/tempo and re-run
```

These are the four State Fair songs with tracks, numbered by their place in the set. The chords follow the charts in the Lyrics and Chords folder. Bar counts are best guesses from the lyric lines: if a section runs long or short at rehearsal, fix its chord list in `make_tracks.py` and re-run.

### Why they sound played, not programmed

- **Timing.** Kick sits a hair ahead of the beat, snare a hair behind, the way a relaxed drummer plays. Every hit has a few milliseconds of random drift.
- **Velocity.** Downbeats are louder than upbeats. No two hits are the same.
- **Ghost notes.** Quiet snare taps between the backbeats in verses and choruses.
- **Fills.** The last bar of each section rolls into the next one.
- **Bass that walks.** Root on the one, fifth in the middle, and a half-step approach note into the next chord.

The real secret is the sound source. A good sampled acoustic kit turns these notes into a drummer; a cheap one makes them sound like a keyboard demo. See Lesson 2.

---

## The lesson plan

Five sessions, about an hour each. Do them in order.

### Lesson 1: Find your way around (no music yet)

1. Open Live. Press **Tab** a few times. That flips between **Session View** (a grid of clips, for playing live) and **Arrangement View** (a timeline, for recording). You'll live in Session View.
2. In Session View, each **column is a track** (drums, bass). Each **row is a scene** (a section of the song). The buttons on the far right launch a whole row at once.
3. Top-left of the screen: the **tempo** box and the **metronome** button. Top-right-ish: the **quantization** menu, which should read **1 Bar**. That setting is what makes everything land in time: press a button any time during a bar and it waits for the next downbeat.
4. Space bar starts and stops. Get comfortable with that before anything else.

**Homework:** Open the demo song that ships with Live (look under Packs > Core Library in the browser) and click clips on and off. Notice nothing ever lands off-beat.

### Lesson 2: Build the rig (one-time setup)

1. Create three MIDI tracks: **Ctrl+Shift+T**. Name them `Drums`, `Bass` and `Lights` (double-click the name). Lights setup is in `LIGHTING.md`.
2. **Install the Suite packs** (Packs in the left sidebar): Core Library, Session Drums Club, Session Drums Studio, Drum Booth.
3. **Drum sound.** Drag a **Session Drums Studio** kit onto the Drums track. For quiet acoustic songs, try a **Drum Booth** kit instead. If you add **EZdrummer 3** later, it uses the same note map as these files.
4. **Bass sound.** Suite's basses lean synthetic. Start with free **Ample Bass P Lite**. The planned upgrade is **Toontrack EZbass**, which can write a bass line that matches a drum groove.
5. **Audio settings:** Options > Preferences > Audio. Driver type **ASIO** (Windows). Pick your audio interface. Set the buffer size to **128 samples**. Lower means less delay between pressing a button and hearing it; if you hear crackles, go up to 256.

**Homework:** Play the drum track with the computer keyboard (press **M** to turn on the computer MIDI keyboard). Find the kick, snare and hi-hat.

### Lesson 3: Load a song

1. Set the tempo box to the song's tempo (**88** for Paper Stars). Live doesn't read tempo from dragged MIDI files.
2. From your computer's file browser, drag `1-intro-drums.mid` into the **first slot** of the Drums track, `2-verse-drums.mid` into the second slot, and so on down to the outro. Do the same for the bass files in the Bass track.
3. Drag the fill clip (the highest-numbered file) into the last slot of the Drums track.
4. Name the scenes: right-click the scene button on the right > Rename. `Intro`, `Verse`, `Pre-chorus`, `Chorus`, `Bridge`, `Outro`, `Fill`.
5. Launch the Intro scene. It loops. Launch Verse whenever you're ready: it switches on the next bar. Do this until it feels boring.

**Homework:** Play the whole song with your guitar and her voice, you launching scenes by hand. Stretch the verse once, skip the bridge once.

### Lesson 4: Hands-free control

You can't reach for a laptop mid-song. Map the scenes to a foot controller.

1. Plug in a USB MIDI foot controller (anything from a basic 4-switch pedal up to a Morningstar or Behringer FCB works). Turn it on in Preferences > Link, Tempo & MIDI: set **Track** and **Remote** to On for that device.
2. Press **Ctrl+M**. The screen turns blue: this is **MIDI Map mode**.
3. Click a scene launch button, then stomp a footswitch. Repeat for each scene. Press Ctrl+M again to exit.
4. No pedal yet? **Ctrl+K** does the same thing with computer keys. Map Intro to 1, Verse to 2, and so on.
5. Map one switch to the **Stop All Clips** button (the square at the bottom of the scene column) for a hard stop.

**The fill trick:** Press the Fill switch during the last bar of a section. The fill plays for exactly one bar. During that bar, press the next section. It lands right on the downbeat, like the drummer saw you nod.

**Sit-in players: mute, don't stop.** When a drummer or bassist sits in, turn that track off with its **Track Activator** (the numbered button at the bottom of the track). The clips keep running silently, so the other track and the lights stay in time, and switching back on mid-song lands in place. Map each activator to a key with **Ctrl+K** (for example `D` for drums, `B` for bass). If the pedal has spare switches or a second bank, map them there instead. Don't use `"bass": False` in `make_tracks.py` for this; that removes the bass clips for good. Keep both tracks built for every song and decide on the night.

**Homework:** Run a full song without touching the laptop.

### Lesson 5: Gig-ready

1. **One song per set.** Save each song as its own Live Set (File > Save Live Set As), or stack songs vertically in one set with a gap scene between them and a tempo in each scene name (Live changes tempo when a scene name includes it, like `Verse 96 BPM`).
2. **Freeze the tracks** before a gig (right-click the track > Freeze Track). This renders the instruments to audio so the computer does less work and nothing glitches.
3. **Count-in.** Add a scene at the top with only a 1-bar click, or turn on the metronome with a 1-bar count-in (the count-in menu next to the metronome).
4. **Click in your ears, not the crowd's.** With a 4-output audio interface, send the metronome to a headphone output via the **Cue Out** in the Master track, and the backing tracks to the PA. Worth it once you're comfortable.
5. **Mix quieter than you think.** Backing tracks should sit under you two, not on top. Start the drums at about -12 dB on the track fader and the bass a little under that.
6. Turn off Wi-Fi, notifications and auto-updates on gig night.

---

## Adjusting the grooves yourself

Double-click any clip to open the note editor. Things to try:

- **Too busy?** Delete the ghost notes (the very quiet snare hits). In the clip view, the velocity lane at the bottom shows how hard each note is.
- **Wrong chord?** Drag bass notes up or down. Each row is a half step.
- **Want more swing?** Open the **Groove Pool** (the wavy-line icon at the bottom-left of the browser), drag a swing groove onto a clip, and turn up the amount.

## Changing songs with the generator

If you have Python installed, edit `SONGS` at the top of `make_tracks.py` and run:

```
python3 make_tracks.py
```

Each song needs a name, tempo, feel (`straight` or `shuffle`) and one chord per bar for each section. Style can be `light`, `verse`, `chorus` or `ending`. Or skip all that and send me the chord charts.
