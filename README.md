# IPFlix Demo Playlist

Demo playlist for IPFlix app screenshots, testing, and unit tests. Contains 97 channels across 17 categories with real free-to-air live streams, classic movies/series with TMDB posters, and real EPG data from i.mjh.nz.

## Load in the App

**Playlist URL (add as M3U playlist):**
```
https://raw.githubusercontent.com/HalberdLLC/demo-list/main/demo.m3u
```

**EPG URL (auto-detected from playlist header):**
```
https://i.mjh.nz/all/epg.xml.gz
```

The `x-tvg-url` header in the M3U file points to the EPG source. The app auto-detects it during onboarding.

## Categories

### Live TV (57 channels — all with real EPG)
| Category | Count | Channels |
|----------|-------|----------|
| News | 10 | Al Jazeera, BBC News, France 24, DW, Euronews, ABC News, Sky News, CNN, CNA, 7NEWS |
| Entertainment | 19 | Below Deck, MythBusters, True Crime, Paranormal, Bravo, BBC Comedy, HGTV, Bondi Rescue, BBC Top Gear, Dance Moms, The Block, Australia's Got Talent... |
| Sports | 8 | Racing.com, Cricket Gold, LIV Golf, Racing WA, Sky Racing 1/2/Thoroughbred, ABC Sport |
| Documentary | 9 | BBC Earth, Sharks & Predators, BBC Antiques Roadshow, BBC Home & Garden, BBC Food, Cooking & Culture, Yorkshire Vet, Better Homes & Gardens, Bondi Vet |
| Kids | 7 | Nickelodeon, Nick Jr, NickToons, NickToons 90s, NickTeen, ABC Kids, Eden |
| Music | 4 | MTV Ridiculousness, Geordie Shore, Jersey Shore, MTV Reality |

### Movies (20 channels — TMDB metadata, Big Buck Bunny playback)
| Category | Count | Films |
|----------|-------|-------|
| Action Movies | 5 | The Matrix, The Dark Knight, Gladiator, The Lord of the Rings, Saving Private Ryan |
| Crime Movies | 5 | Pulp Fiction, The Godfather, The Godfather Part II, Goodfellas, The Departed |
| Drama Movies | 4 | Fight Club, Schindler's List, Forrest Gump, The Shawshank Redemption, Whiplash |
| Thriller Movies | 2 | The Silence of the Lambs, Se7en |
| Sci-Fi Movies | 2 | Inception, Interstellar |

### Series (20 channels — TMDB metadata, Big Buck Bunny playback)
| Category | Count | Shows |
|----------|-------|-------|
| Crime Series | 6 | Breaking Bad, Peaky Blinders, Narcos, Money Heist, Ozark, The Sopranos |
| Sci-Fi Series | 5 | Stranger Things, The Mandalorian, The Last of Us, Dark, Black Mirror |
| Comedy Series | 3 | The Office, Friends, Wednesday |
| Thriller Series | 2 | Squid Game, Sherlock |
| Fantasy Series | 2 | Game of Thrones, The Witcher |
| Drama Series | 2 | The Crown, Chernobyl |

## EPG Source

All 57 live channels use `tvg-id` values matching [i.mjh.nz](https://i.mjh.nz) channel IDs. Real programme data (titles, descriptions, times) is provided automatically.

EPG URL: `https://i.mjh.nz/all/epg.xml.gz` (gzipped XMLTV, ~3MB, updated daily)

## Files

- `demo.m3u` — M3U playlist with 97 channels
- `epg.xml` — Legacy XMLTV EPG (not needed — i.mjh.nz provides real data)
- `generate_epg.py` — Legacy EPG generator (not needed)
