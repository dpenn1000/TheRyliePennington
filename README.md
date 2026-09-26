# Daddy Long Legs: live rig

Backing tracks, lighting and show control for the daddy-daughter duo [Daddy Long Legs](https://daddylonglegsband.com).

- **[ableton/README.md](ableton/README.md)**: learn Ableton in 5 lessons and load the backing tracks
- **[ableton/LIGHTING.md](ableton/LIGHTING.md)**: Ableton → ONYX → Blizzard LB-Hex pars
- **[ableton/BANDHELPER.md](ableton/BANDHELPER.md)**: BandHelper on Android, plus AbleSet
- **[docs/GIG-PLAN.md](docs/GIG-PLAN.md)**: Arizona State Fair plan and gig-day checklist
- **[docs/RESEARCH.md](docs/RESEARCH.md)**: what we looked into and why
- **[CLAUDE.md](CLAUDE.md)**: project context and open tasks for Claude sessions

## Regenerate the backing tracks

```
cd ableton
python3 make_tracks.py
```

Edit the `SONGS` list at the top of `make_tracks.py` first. Each song needs a tempo, a feel (`straight` or `shuffle`) and one chord per bar for each section.
