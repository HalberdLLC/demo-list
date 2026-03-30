# IPFlix Demo Playlist

Demo playlist for IPFlix app screenshots, testing, and unit tests. Contains 68 channels across 8 categories with real free-to-air live streams and Creative Commons licensed films (Blender Foundation open movies).

## Load in the App

**Playlist URL (add as M3U playlist):**
```
https://raw.githubusercontent.com/HalberdLLC/demo-list/main/demo.m3u
```

**EPG URL (auto-detected from playlist header):**
```
https://raw.githubusercontent.com/HalberdLLC/demo-list/main/epg.xml
```

The `x-tvg-url` header in the M3U file points directly to the EPG, so the app will auto-suggest the EPG source during onboarding.

## Categories

| Category | Count | Type |
|----------|-------|------|
| News | 10 | Live streams (Al Jazeera, DW, France 24, BBC, Euronews, ...) |
| Sports | 9 | Live streams (CBS Sports, ESPN8, Cricket Gold, DAZN Combat, ...) |
| Entertainment | 8 | Live streams (BET, MTV, Cozi TV, Pluto Animation, ...) |
| Kids | 7 | Live streams (PBS Kids, Baby Shark TV, ABC Kids, Disney Jr., ...) |
| Music | 8 | Live streams (MTV Pop, CMT, Stingray Jazz, NOW Rock, ...) |
| Movies | 10 | Blender Foundation open movies (Big Buck Bunny, Sintel, Tears of Steel, ...) — CC licensed |
| Series | 8 | Blender Open Movies series (S01E01-E04, S02E01-E04) — CC licensed |
| Documentary | 8 | Live streams (BBC Earth, Nat Geo, History Channel, ...) |

## Regenerate EPG

EPG data uses dates relative to the current day. Regenerate before screenshot sessions to ensure all time slots cover the current time:

```bash
cd demo
python3 generate_epg.py
```

> **Note:** EPG data is date-relative. Regenerate before screenshot sessions.

## Files

- `demo.m3u` — M3U playlist with 70 channels
- `epg.xml` — XMLTV EPG file with 3 days of programme data (yesterday through tomorrow)
- `generate_epg.py` — Python script to regenerate `epg.xml` with fresh dates
