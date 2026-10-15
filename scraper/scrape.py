
import json
import re
from pathlib import Path
from urllib.parse import urlparse
from urllib.robotparser import RobotFileParser

import requests
from bs4 import BeautifulSoup
from dotenv import load_dotenv
from google import genai

SOURCE_URL = (
    "https://ibets.co.za/guides-and-tips/"
    "new-online-casinos-south-africa/"
)
CASINOS = ["Carousel Casino", "Virgin Bet", "Bettabets"]
USER_AGENT = "CasinoBonusScraper/1.0 (screening project)"
OUTPUT = Path(__file__).resolve().parents[1] / "docs" / "bonuses.json"


def fetch_page():
    parsed = urlparse(SOURCE_URL)
    robots_url = f"{parsed.scheme}://{parsed.netloc}/robots.txt"

    response = requests.get(
        robots_url,
        headers={"User-Agent": USER_AGENT},
        timeout=15,
    )
    response.raise_for_status()

    robots = RobotFileParser()
    robots.parse(response.text.splitlines())

    if not robots.can_fetch(USER_AGENT, SOURCE_URL):
        raise PermissionError("Scraping not allowed by robots.txt")

    response = requests.get(
        SOURCE_URL,
        headers={"User-Agent": USER_AGENT},
        timeout=20,
    )
    response.raise_for_status()
    return BeautifulSoup(response.text, "html.parser")


def extract_sections(soup):
    sections = {}

    for heading in soup.find_all("h3"):
        name = heading.get_text(" ", strip=True)
        if name not in CASINOS:
            continue

        pieces = []
        for element in heading.next_elements:
            if getattr(element, "name", None) in ("h2", "h3"):
                break
            if isinstance(element, str):
                value = element.strip()
                if value:
                    pieces.append(value)

        sections[name] = " ".join(pieces)[:5000]

    missing = set(CASINOS) - set(sections)
    if missing:
        raise ValueError(f"Casino sections not found: {missing}")

    return sections




def extract_with_ai(name, terms, client):
    instructions = (
        "Extract the welcome bonus information for the named casino "
        "from the supplied website text. Return a JSON object with "
        "exactly three keys: welcome_bonus, wagering_multiplier, "
        "minimum_deposit. "
        "Return null for wagering_multiplier if only sports betting "
        "rollover is stated. Do not use sports rollover as casino wagering. "
        "welcome_bonus and minimum_deposit must be strings or null. "
        "wagering_multiplier must be a number or null. "
        "Use the wagering requirement applicable to the casino bonus. "
        "Do not confuse a sports betting rollover with casino wagering. "
        "The minimum deposit must be the amount required to qualify "
        "for the welcome bonus, not simply a general account deposit. "
        "If any field is absent or ambiguous, use null. "
        "Never invent information."
    )

    response = client.models.generate_content(
        model="gemini-3.5-flash-lite",
        contents=f"{instructions}\n\nCasino: {name}\nSource text:\n{terms}",
        config={"response_mime_type": "application/json"},
    )

    if not response.text:
        raise ValueError(f"Gemini returned no text for {name}")

    result = json.loads(response.text)

    expected = (
        "welcome_bonus",
        "wagering_multiplier",
        "minimum_deposit",
    )

    if any(key not in result for key in expected):
        raise ValueError(f"Missing Gemini fields for {name}")

    multiplier = result["wagering_multiplier"]

    if multiplier is not None and (
        isinstance(multiplier, bool)
        or not isinstance(multiplier, (int, float))
    ):
        raise ValueError(f"Invalid multiplier for {name}")

    return {
        "casino": name,
        "welcome_bonus": result["welcome_bonus"],
        "wagering_multiplier": multiplier,
        "minimum_deposit": result["minimum_deposit"],
        "source_url": SOURCE_URL,
       
    }



def main():
    load_dotenv()

    print("Checking robots.txt and downloading source...")
    soup = fetch_page()
    sections = extract_sections(soup)
    client =  genai.Client()

    results = []
    for name in CASINOS:
        print(f"Extracting bonus information for {name}...")
        result = extract_with_ai(name, sections[name], client)
        results.append(result)

    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT.write_text(
        json.dumps(results, indent=2, ensure_ascii=False),
        encoding="utf-8",
    )

    print(f"Success! Saved {len(results)} casinos to {OUTPUT}")


if __name__ == "__main__":
    main()
