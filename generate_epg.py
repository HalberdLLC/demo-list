#!/usr/bin/env python3
"""
IPFlix Demo EPG Generator
Generates XMLTV EPG data for all channels in demo.m3u.
Run: python3 generate_epg.py
Output: epg.xml (in same directory as this script)
"""

import re
import os
from datetime import datetime, timedelta, timezone

# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))


def xmltv_time(dt: datetime) -> str:
    """Format a UTC datetime as XMLTV timestamp: YYYYMMDDHHmmss +0000"""
    return dt.strftime("%Y%m%d%H%M%S +0000")


def xml_escape(text: str) -> str:
    """Escape special XML characters."""
    return (
        text.replace("&", "&amp;")
        .replace("<", "&lt;")
        .replace(">", "&gt;")
        .replace('"', "&quot;")
        .replace("'", "&apos;")
    )


# ---------------------------------------------------------------------------
# Parse demo.m3u
# ---------------------------------------------------------------------------

def parse_m3u(path: str) -> list[dict]:
    """Parse demo.m3u and return list of channel dicts."""
    channels = []
    with open(path, encoding="utf-8") as f:
        lines = f.readlines()

    for line in lines:
        if not line.startswith("#EXTINF"):
            continue
        tvg_id = re.search(r'tvg-id="([^"]+)"', line)
        tvg_name = re.search(r'tvg-name="([^"]+)"', line)
        tvg_logo = re.search(r'tvg-logo="([^"]+)"', line)
        group = re.search(r'group-title="([^"]+)"', line)
        if not tvg_id:
            continue
        channels.append({
            "id": tvg_id.group(1),
            "name": tvg_name.group(1) if tvg_name else tvg_id.group(1),
            "logo": tvg_logo.group(1) if tvg_logo else "",
            "category": group.group(1) if group else "General",
        })

    return channels


# ---------------------------------------------------------------------------
# Programme templates per category
# ---------------------------------------------------------------------------

PROGRAMMES = {
    "News": {
        "duration_minutes": 30,
        "titles": [
            "Morning Report",
            "World News Update",
            "Breaking Headlines",
            "Business Today",
            "Evening Bulletin",
            "Late Night Wrap",
            "Politics Now",
            "Global Roundup",
            "Special Report",
            "Weekend Edition",
        ],
        "descriptions": [
            "Comprehensive coverage of today's top stories from around the world.",
            "In-depth analysis of global events and breaking news.",
            "Headlines and updates from our international correspondents.",
            "Financial markets, economic news, and business analysis.",
            "A summary of today's most important news events.",
            "Late night review of the day's news with expert commentary.",
            "Political news and analysis from capitals around the world.",
            "Stories from every corner of the globe.",
            "An in-depth look at a developing story.",
            "News and features for the weekend audience.",
        ],
    },
    "Sports": {
        "duration_minutes": 75,
        "titles": [
            "Live Match Coverage",
            "Sports Center",
            "Highlights Show",
            "Sports Talk Live",
            "Championship Preview",
            "Match of the Day",
            "Post-Game Analysis",
            "Weekend Sports Wrap",
        ],
        "descriptions": [
            "Live coverage of today's match with commentary and analysis.",
            "Sports news, scores, and highlights from today's events.",
            "Extended highlights from the best action of the day.",
            "Sports journalists discuss the biggest stories in sport.",
            "Preview and predictions for this weekend's big games.",
            "The best matches and goals from today's football.",
            "Expert analysis of today's results and performances.",
            "A wrap of all the major sports stories this weekend.",
        ],
    },
    "Entertainment": {
        "duration_minutes": 60,
        "titles": [
            "Comedy Hour",
            "Late Night Show",
            "Reality TV",
            "Game Show",
            "Talk Show Live",
            "Variety Special",
            "Celebrity News",
            "Best Of Entertainment",
        ],
        "descriptions": [
            "An hour of the best comedy clips and stand-up performances.",
            "Your favourite late night host with guests and monologue.",
            "Follow real people in unscripted entertainment.",
            "Contestants compete for prizes in today's game show.",
            "Your favourite host interviews celebrities and pop culture figures.",
            "Music, comedy, and special performances in a variety format.",
            "The latest gossip and news from the world of celebrity.",
            "A curated selection of the best entertainment moments.",
        ],
    },
    "Kids": {
        "duration_minutes": 30,
        "titles": [
            "Cartoon Time",
            "Adventure Show",
            "Fun Learning",
            "Animal Friends",
            "Story Time",
            "Music & Dance",
            "Art & Craft",
            "Super Heroes",
        ],
        "descriptions": [
            "Colourful animated adventures for kids of all ages.",
            "Join our heroes on exciting adventures around the world.",
            "Fun and interactive educational content for young minds.",
            "Discover amazing animals and their natural habitats.",
            "Classic and new stories read aloud with beautiful illustrations.",
            "Sing, dance, and move along with your favourite characters.",
            "Creative projects and art activities for young artists.",
            "Action-packed adventures with beloved super heroes.",
        ],
    },
    "Music": {
        "duration_minutes": 60,
        "titles": [
            "Top Hits Live",
            "Rock Classics",
            "Pop Countdown",
            "Jazz Hour",
            "Music Awards",
            "Artist Spotlight",
            "Country Gold",
            "Rhythm & Blues",
        ],
        "descriptions": [
            "Today's biggest hits played back to back.",
            "The greatest rock anthems of all time.",
            "Counting down the hottest pop songs of the week.",
            "Smooth jazz standards performed by master musicians.",
            "Celebrating the best in music with live award performances.",
            "An in-depth look at the life and music of a great artist.",
            "The best of country music from past and present.",
            "Soul and R&B classics and contemporary hits.",
        ],
    },
    "Movies": {
        "duration_minutes": 120,
        "titles": [
            "The Matrix",
            "Inception",
            "Interstellar",
            "The Dark Knight",
            "Pulp Fiction",
            "Fight Club",
            "Gladiator",
            "The Godfather",
            "Schindler's List",
            "Forrest Gump",
        ],
        "descriptions": [
            "A computer hacker discovers the reality he lives in is a simulation and joins rebels fighting AI overlords.",
            "A thief who steals corporate secrets through dream-sharing technology is given a task to plant an idea.",
            "Astronauts travel through a wormhole near Saturn to find a new home for humanity.",
            "Batman faces the Joker, a criminal mastermind who wants to plunge Gotham into anarchy.",
            "The lives of two mob hit men, a boxer, and others intertwine in four tales of violence and redemption.",
            "An insomniac office worker forms an underground fight club with a soap salesman.",
            "A former Roman general seeks revenge against the corrupt emperor who murdered his family.",
            "The aging patriarch of an organized crime dynasty transfers control of his clandestine empire to his son.",
            "A Polish-Jewish businessman tries to save his workers during the Holocaust.",
            "The story of a man with a low IQ who witnesses and influences several defining historical events in the US.",
        ],
    },
    "Series": {
        "duration_minutes": 45,
        "titles": [
            "Breaking Bad",
            "Game of Thrones",
            "Stranger Things",
            "The Office",
            "Friends",
            "The Crown",
            "The Mandalorian",
            "Wednesday",
            "Squid Game",
            "The Witcher",
        ],
        "descriptions": [
            "A high school chemistry teacher turns to manufacturing methamphetamine when diagnosed with cancer.",
            "Nine noble families fight for control over the mythical lands of Westeros.",
            "A group of kids encounter supernatural forces and government conspiracies in a small town.",
            "A mockumentary about the everyday lives of office employees in a paper company.",
            "A group of six friends navigate life and love in Manhattan.",
            "A dramatisation of the reign of Queen Elizabeth II from the 1940s to modern times.",
            "A Mandalorian bounty hunter navigates the far reaches of the galaxy.",
            "The daughter of Gomez and Morticia Addams attends Nevermore Academy.",
            "Hundreds of cash-strapped players accept an invitation to compete in children's games for a prize.",
            "A mutated monster hunter struggles to find his place in a world where people often dread monsters.",
        ],
    },
    "Documentary": {
        "duration_minutes": 60,
        "titles": [
            "Planet Earth",
            "Ocean Wonders",
            "Human History",
            "Space Exploration",
            "Wildlife Safari",
            "Ancient Civilizations",
            "Technology Frontiers",
            "Climate Earth",
        ],
        "descriptions": [
            "Stunning footage of Earth's most breathtaking natural environments and the animals that inhabit them.",
            "Dive into the depths of the ocean and discover incredible marine life.",
            "A journey through the milestones of human civilisation from prehistory to today.",
            "The story of humanity's greatest adventure beyond our home planet.",
            "Follow wildlife rangers and researchers as they monitor animals in the wild.",
            "Uncover the mysteries of ancient cultures and forgotten empires.",
            "Explore the cutting-edge discoveries that are reshaping our world.",
            "Examining the causes and consequences of climate change on our planet.",
        ],
    },
}


# ---------------------------------------------------------------------------
# Generate programme schedule for a channel
# ---------------------------------------------------------------------------

def generate_schedule(channel: dict, start: datetime, end: datetime) -> list[dict]:
    """Generate contiguous programme slots for a channel over the given range."""
    cat = channel["category"]
    template = PROGRAMMES.get(cat, PROGRAMMES["News"])
    duration = timedelta(minutes=template["duration_minutes"])
    titles = template["titles"]
    descs = template["descriptions"]

    programmes = []
    current = start
    idx = 0
    while current < end:
        slot_end = min(current + duration, end)
        title = titles[idx % len(titles)]
        desc = descs[idx % len(descs)]

        # For Movies/Series: inject channel-specific title for variety
        if cat == "Movies":
            title = titles[idx % len(titles)]
            desc = descs[idx % len(descs)]
        elif cat == "Series":
            base_title = titles[idx % len(titles)]
            season = (idx // len(titles)) + 1
            episode = (idx % len(titles)) + 1
            title = base_title
            desc = f"Season {season}, Episode {episode}. " + descs[idx % len(descs)]

        programmes.append({
            "start": current,
            "stop": slot_end,
            "channel": channel["id"],
            "title": title,
            "desc": desc,
            "category": cat,
        })
        current = slot_end
        idx += 1

    return programmes


# ---------------------------------------------------------------------------
# Write XMLTV file
# ---------------------------------------------------------------------------

def write_xmltv(channels: list[dict], all_programmes: list[dict], output_path: str) -> None:
    with open(output_path, "w", encoding="utf-8") as f:
        f.write('<?xml version="1.0" encoding="UTF-8"?>\n')
        f.write('<!DOCTYPE tv SYSTEM "xmltv.dtd">\n')
        f.write('<tv source-info-name="IPFlix Demo EPG" generator-info-name="ipflix-demo">\n\n')

        # Channel elements
        for ch in channels:
            f.write(f'  <channel id="{xml_escape(ch["id"])}">\n')
            f.write(f'    <display-name lang="en">{xml_escape(ch["name"])}</display-name>\n')
            if ch["logo"]:
                f.write(f'    <icon src="{xml_escape(ch["logo"])}"/>\n')
            f.write(f'  </channel>\n')

        f.write("\n")

        # Programme elements
        for prog in all_programmes:
            start_str = xmltv_time(prog["start"])
            stop_str = xmltv_time(prog["stop"])
            f.write(f'  <programme start="{start_str}" stop="{stop_str}" channel="{xml_escape(prog["channel"])}">\n')
            f.write(f'    <title lang="en">{xml_escape(prog["title"])}</title>\n')
            f.write(f'    <desc lang="en">{xml_escape(prog["desc"])}</desc>\n')
            f.write(f'    <category lang="en">{xml_escape(prog["category"])}</category>\n')
            f.write(f'  </programme>\n')

        f.write("</tv>\n")


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def main():
    m3u_path = os.path.join(SCRIPT_DIR, "demo.m3u")
    epg_path = os.path.join(SCRIPT_DIR, "epg.xml")

    channels = parse_m3u(m3u_path)
    print(f"Parsed {len(channels)} channels from demo.m3u")

    # Generate 3 days: yesterday 00:00 UTC → tomorrow+1 00:00 UTC
    now_utc = datetime.now(tz=timezone.utc)
    start = datetime(now_utc.year, now_utc.month, now_utc.day, 0, 0, 0, tzinfo=timezone.utc) - timedelta(days=1)
    end = start + timedelta(days=3)

    all_programmes = []
    for ch in channels:
        progs = generate_schedule(ch, start, end)
        all_programmes.extend(progs)

    print(f"Generated {len(all_programmes)} programme entries")

    write_xmltv(channels, all_programmes, epg_path)
    print(f"EPG written to {epg_path}")


if __name__ == "__main__":
    main()
