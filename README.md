# casino-bonus-scraper
Working task.
### Development Time

**Total active development time:** [Insert actual hours and minutes]

The project was completed as a time-boxed technical assessment. Active development time includes environment setup, source research, scraper implementation, AI integration, testing, website deployment and documentation.

Breaks and periods when no project work was undertaken are excluded.


# BonusScope - AI Casino Bonus Scraper

A Python scraper and responsive web page built for a
time-boxed technical screening assessment.

## Overview

The application extracts welcome bonus information for
three online casinos from one publicly accessible comparison
article. Google Gemini converts unstructured promotional text
into structured JSON. The website displays the generated data.

## Source

https://ibets.co.za/guides-and-tips/new-online-casinos-south-africa/

Casinos:
- Carousel Casino
- Virgin Bet
- Bettabets

## Technology

- Python 3
- Requests
- Beautiful Soup
- Google Gemini API
- HTML, CSS and JavaScript
- GitHub Pages

## Installation

1. Clone the repository.
2. Open a terminal in the repository folder.
3. Install dependencies:

   python -m pip install -r requirements.txt

4. Create a .env file containing:

   GEMINI_API_KEY=your_api_key_here

5. Run the scraper:

   python -m scraper.scrape

The script checks robots.txt, fetches the public article,
extracts the casino text, calls Gemini and generates
docs/bonuses.json.

## Website

The website is hosted using GitHub Pages from the /docs folder.

https://retha01.github.io/casino-bonus-scraper/

For local testing, run:

   python -m http.server 8000 --directory docs

Then open http://localhost:8000

## Limitations

- Data accuracy depends on the source article.
- Offers may change without notice.
- Sports rollover and casino wagering requirements may differ.
- Unavailable values should be reported as null rather
  than invented.
- The website displays the most recently generated JSON.
  It does not run the scraper automatically.
- API access requires available Gemini quota.

## Responsible Scraping

The script checks robots.txt before retrieving the page.
It does not bypass logins, CAPTCHAs or access restrictions.

## Development Time

Actual active development time: [ENTER ACTUAL TIME]

Incomplete items at the three-hour limit:
[ENTER ANY UNFINISHED ITEMS OR WRITE NONE]
