# IPFlix Demo Playlist

Demo playlist for IPFlix app screenshots, testing, and unit tests. Contains 60 channels across 7 categories with real free-to-air live streams, classic movies with TMDB posters, and real EPG data from i.mjh.nz.

## Load in the App

**Playlist URL (add as M3U playlist):**
```
https://raw.githubusercontent.com/HalberdLLC/demo-list/main/demo.m3u
```

**EPG URL (auto-detected from playlist header):**
```
https://i.mjh.nz/all/epg.xml.gz
```

The `x-tvg-url` header in the M3U file points to the EPG source. The app auto-detects it during onboarding — no manual entry needed.

## Categories

| Category | Count | Type |
|----------|-------|------|
| News | 10 | Live streams with real EPG (Al Jazeera, BBC News, France 24, DW, Euronews, ABC News, Sky News, CNN, CNA, 7NEWS) |
| Sports | 8 | Live streams with real EPG (Racing.com, Cricket Gold, LIV Golf, Racing WA, Sky Racing 1/2/Thoroughbred, ABC Sport) |
| Entertainment | 12 | Live streams with real EPG (Below Deck, MythBusters, True Crime, Paranormal, Motorheads, Deadliest Catch, House Hunters, Bravo, 10 Comedy/Drama, 7Bravo, BBC Comedy) |
| Kids | 6 | Live streams with real EPG (Nickelodeon, Nick Jr, NickToons, NickToons 90s, NickTeen, ABC Kids) |
| Music | 4 | Live streams with real EPG (MTV Ridiculousness, Geordie Shore, Jersey Shore, MTV Reality) |
| Movies | 15 | Classic films with TMDB posters (The Matrix, Inception, Interstellar, The Dark Knight, Pulp Fiction, Fight Club, Gladiator, The Godfather, Schindler's List, Forrest Gump, The Shawshank Redemption, The Lord of the Rings, Goodfellas, Saving Private Ryan, The Silence of the Lambs) |
| Documentary | 5 | Live streams with real EPG (BBC Earth, Sharks & Predators, BBC Antiques Roadshow, BBC Home & Garden, BBC Food) |

## EPG Source

All 45 live channels use `tvg-id` values matching [i.mjh.nz](https://i.mjh.nz) channel IDs. Real programme data (titles, descriptions, times) is provided automatically.

EPG URL: `https://i.mjh.nz/all/epg.xml.gz` (gzipped XMLTV, ~3MB, updated daily)

## Files

- `demo.m3u` — M3U playlist with 60 channels (45 live + 15 movies)
- `epg.xml` — Legacy XMLTV EPG (not needed — i.mjh.nz provides real data)
- `generate_epg.py` — Legacy EPG generator (not needed — i.mjh.nz provides real data)
