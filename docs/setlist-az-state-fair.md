# Arizona State Fair set list

Sunday, October 4, 2026, 1:00 to 2:00 pm. One set, 14 songs. BandHelper totals it at 54:46; the song durations alone add up to 51:31.

Pulled from BandHelper on September 26, 2026. "Chart shapes" is what the guitar chart is written in. Where it differs from the key, a capo is doing the rest. The bass tracks need the sounding key, so the capo column has to be right before a song goes into `make_tracks.py`.

| # | Song | Original or cover | Key (BandHelper) | Chart shapes | Capo | Tempo | Time | Length |
|---|---|---|---|---|---|---|---|---|
| 1 | Country Roads | Cover, John Denver | A | none on file | ? | 66 | ? | 3:10 |
| 2 | Halfway Gone, Halfway Brave | Original | A (BandHelper and chart still say Ab) | G | 2 | 104 | 4/4 | 3:15 |
| 3 | Big Yellow Taxi | Cover, Joni Mitchell | D | G | ? | ? | ? | 2:16 |
| 4 | House of the Rising Sun | Cover, The Animals | Am | Am | ? | ? | ? (6/8 on the record) | 4:20 |
| 5 | Trains I Missed | Cover, Balsam Range | B | A (capo 2) | 2 | ? | ? | 3:48 |
| 6 | Choosin' Texas | Cover, Ella Langley | Db | C | 1 | 110 | 4/4 | 3:50 |
| 7 | Kiss Me | Cover, Sixpence None The Richer | Eb | D | 1 | 100 | 4/4 | 3:24 |
| 8 | These Old Wheels | Cover, Mandolin Orange | ? | G | ? | ? | ? | 2:36 |
| 9 | Melissa | Cover, Allman Brothers | E | E | none | 83 (record) | 4/4 | 3:54 |
| 10 | Paper Stars | Original | Db | C | 1 | 88 | 4/4 | 5:00 |
| 11 | Starting Over | Cover, Chris Stapleton | G | G | ? | ? | ? | 4:00 |
| 12 | Need You Now | Cover, Lady Antebellum | ? | F / Am / C | ? | ? | ? | 3:56 |
| 13 | Valerie | Cover, The Zutons | Eb | Eb | ? | ? | ? | 3:39 |
| 14 | Radio GaGa | Cover, Queen | E | E | none | ? (record is about 112) | 4/4 | 4:23 |

## Chord charts

| Song | Where the chart is | Chords per section |
|---|---|---|
| Country Roads | Bass PDF only (UG link, no chord text); no chords in BandHelper | Missing |
| Halfway Gone, Halfway Brave | `Halfway Gone, Halfway Brave.txt` + BandHelper | Complete |
| Big Yellow Taxi | `Big Yellow Taxi.docx` | First verse and chorus only |
| House of the Rising Sun | `House of the Rising Sun.docx` | Complete (one progression throughout) |
| Trains I Missed | `Trains I Missed.docx`, plus a capo-4 version | Verse and chorus |
| Choosin' Texas | `Choosin Texas.txt` + BandHelper | Complete |
| Kiss Me | `Kiss Me.txt` + BandHelper | Complete |
| These Old Wheels | BandHelper lyrics (the .docx is empty) | Complete: every verse uses verse 1's changes, G C G D/F# Em D/F# C G D/F# G |
| Melissa | Ultimate Guitar official chart (tabs.ultimate-guitar.com, melissa-official-2601657) | Complete, see Song notes |
| Paper Stars | `Paper Stars.txt` + BandHelper | Complete |
| Starting Over | `Starting Over.docx` | Verse and chorus |
| Need You Now | `Need you Now.docx` | Verse, chorus, bridge |
| Valerie | `Valerie.docx` | Verse and chorus |
| Radio GaGa | `Radio Gaga.pdf` (the band's own chart) | Complete, see Song notes |

The charts live in the band's Lyrics and Chords folder on OneDrive, not in this repo.

## Song notes

### Halfway Gone, Halfway Brave

Measured from a September 2026 performance video: about 105 BPM average, verses near 100, choruses pushing toward 110. Track tempo set at **104** so the track sits a hair under her natural pace. Check 100, 104 and 108 at rehearsal.

Plays in **A** (G shapes, capo 2), confirmed Sept 26. The chart and BandHelper still say capo 1, Ab; update them.

One chord per bar. Bar counts from the lyric timings:

| Section | Bars | Chords (chart shapes) |
|---|---|---|
| Verse | 8 | G C Em D, twice |
| Pre-chorus | 6 | Em C G D, D held 2 more bars |
| Chorus | 12 | G C Em D, twice, then C G G G |
| Bridge | 8 | Am G Am D Am C C D (not in the video, estimate) |

The pre-chorus and chorus tail are estimates within about half a bar.

### Melissa

From the Ultimate Guitar official chart: key E, no capo, 83 BPM (the record's tempo). One UG commenter notes Gregg Allman plays it simpler on guitar; the bass track only needs the roots either way.

Bar counts are an estimate at one chord per bar. Check against how you play it.

| Section | Bars | Chords |
|---|---|---|
| Intro | 8 | E F#m11 Emaj7/G# F#m11, twice |
| Verse | 8 | E F#m11 Emaj7/G# F#m11, E E F#m11 F#m11 |
| Chorus | 12 | Asus2 Bsus4 C#m7 Asus2/D, E F#m11 Emaj7/G# F#m11, Cmaj7 Cmaj7 B B |
| Interlude | 4 | E F#m11 Emaj7/G# F#m11 |
| Bridge | 12 | E E Dsus2 Dsus2 Asus2 Asus2 Bsus4 Bsus4 C#m7 C#m7 Asus2 B |
| Outro | 8 | Cmaj7 Cmaj7 B E, then F#m11 Emaj7/G# F#m11 E |

Song order: intro, verse, chorus, interlude, verse, chorus, interlude, bridge, verse, chorus, outro.

### Radio GaGa

From the band's own chart, in E (the record is in F). Tempo not set yet; the record sits around 112.

The chorus changes chord every half bar (A to E on "radio ga ga"), so `make_tracks.py` needs a two-chords-in-one-bar option before this song goes in. Bar counts are an estimate.

| Section | Bars | Chords |
|---|---|---|
| Intro | 6 | E F#m A F#m A E |
| Verse | 16 | E E F#m F#m A A F#m A-E, twice |
| Pre-chorus | 14 | E E C#dim/G C#dim/G, A A Bbdim Bbdim, E/B E/B B B, A E |
| Chorus | 8 | Esus4, A-E, A-E, A-E, Esus4, A-E, F#m A, B C#m B E |

"A-E" is two chords in one bar. Song order: intro, verse, verse, pre-chorus, chorus, verse, pre-chorus (last 2 lines only), chorus x3 lines, outro on the last line.

## Things to settle

- Big Yellow Taxi: BandHelper says D, but the chart is in G shapes. Capo 7, or does one of them need fixing?
- Trains I Missed: capo 2 in B means A shapes. The chart on file is in B shapes (B, F#, G#m, E) and the other version is capo 4, so neither matches yet.
- Need You Now and These Old Wheels have no key in BandHelper.
- Chord timing: some charts need adjusting before their tracks get built.
