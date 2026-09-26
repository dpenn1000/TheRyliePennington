# Arizona State Fair set list

Sunday, October 4, 2026, 1:00 to 2:00 pm. One set, 14 songs. BandHelper totals it at 54:46; the song durations alone add up to 51:31.

Pulled from BandHelper on September 26, 2026. "Chart shapes" is what the guitar chart is written in. Where it differs from the key, a capo is doing the rest. The bass tracks need the sounding key, so the capo column has to be right before a song goes into `make_tracks.py`.

| # | Song | Original or cover | Key (BandHelper) | Chart shapes | Capo | Tempo | Time | Length |
|---|---|---|---|---|---|---|---|---|
| 1 | Country Roads | Cover, John Denver | A | none on file | ? | 66 | ? | 3:10 |
| 2 | Halfway Gone, Halfway Brave | Original | Ab (A in the Sept video) | G | 1 or 2, confirm | 104 | 4/4 | 3:15 |
| 3 | Big Yellow Taxi | Cover, Joni Mitchell | D | G | ? | ? | ? | 2:16 |
| 4 | House of the Rising Sun | Cover, The Animals | Am | Am | ? | ? | ? (6/8 on the record) | 4:20 |
| 5 | Trains I Missed | Cover, Balsam Range | B | A (capo 2) | 2 | ? | ? | 3:48 |
| 6 | Choosin' Texas | Cover, Ella Langley | Db | C | 1 | 110 | 4/4 | 3:50 |
| 7 | Kiss Me | Cover, Sixpence None The Richer | Eb | D | 1 | 100 | 4/4 | 3:24 |
| 8 | These Old Wheels | Cover, Mandolin Orange | ? | G | ? | ? | ? | 2:36 |
| 9 | Melissa | Cover, Allman Brothers | E | E | ? | ? | ? | 3:54 |
| 10 | Paper Stars | Original | Db | C | 1 | 88 | 4/4 | 5:00 |
| 11 | Starting Over | Cover, Chris Stapleton | G | G | ? | ? | ? | 4:00 |
| 12 | Need You Now | Cover, Lady Antebellum | ? | F / Am / C | ? | ? | ? | 3:56 |
| 13 | Valerie | Cover, The Zutons | Eb | Eb | ? | ? | ? | 3:39 |
| 14 | Radio GaGa | Cover, Queen | E | E | ? | ? | ? | 4:23 |

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
| Melissa | `Melissa.docx` | Chorus only; verses show a bare E |
| Paper Stars | `Paper Stars.txt` + BandHelper | Complete |
| Starting Over | `Starting Over.docx` | Verse and chorus |
| Need You Now | `Need you Now.docx` | Verse, chorus, bridge |
| Valerie | `Valerie.docx` | Verse and chorus |
| Radio GaGa | `Radio Gaga.docx` | Verse and chorus |

The charts live in the band's Lyrics and Chords folder on OneDrive, not in this repo.

## Song notes

### Halfway Gone, Halfway Brave

Measured from a September 2026 street-performance video (Old Town Scottsdale): about 105 BPM average, verses near 100, choruses pushing toward 110. Track tempo set at **104** so the track sits a hair under her natural pace. Check 100, 104 and 108 at rehearsal.

The video sounds in **A** (G shapes, capo 2). The chart and BandHelper say capo 1, Ab. Confirm with Rylie before building the bass.

One chord per bar. Bar counts from the lyric timings:

| Section | Bars | Chords (chart shapes) |
|---|---|---|
| Verse | 8 | G C Em D, twice |
| Pre-chorus | 6 | Em C G D, D held 2 more bars |
| Chorus | 12 | G C Em D, twice, then C G G G |
| Bridge | 8 | Am G Am D Am C C D (not in the video, estimate) |

The pre-chorus and chorus tail are estimates within about half a bar.

## Things to settle

- Big Yellow Taxi: BandHelper says D, but the chart is in G shapes. Capo 7, or does one of them need fixing?
- Trains I Missed: capo 2 in B means A shapes. The chart on file is in B shapes (B, F#, G#m, E) and the other version is capo 4, so neither matches yet.
- Need You Now and These Old Wheels have no key in BandHelper.
- Chord timing: some charts need adjusting before their tracks get built.
- Halfway Gone key: A (capo 2) or Ab (capo 1).
