
# Casino Bonus Comparison

A Python-based casino bonus scraper and responsive comparison website
developed for a time-boxed web developer technical assessment.

## Project Overview

The application automatically extracts welcome bonus information for
three online casinos from one publicly accessible comparison article.

Google Gemini processes the unstructured bonus descriptions and
converts them into structured JSON. A responsive webpage reads the
generated JSON file and displays the results in a comparison table.

## Data Source

Source:
https://ibets.co.za/guides-and-tips/new-online-casinos-south-africa/

Casinos included:
- Carousel Casino
- Virgin Bet
- Bettabets

Extracted fields:
- Welcome bonus
- Wagering multiplier
- Minimum deposit
- Source URL

## Technology Stack

- Python 3
- Requests
- Beautiful Soup
- Google Gemini API
- HTML, CSS and JavaScript
- GitHub Pages

## Installation and Setup

Clone the repository:

```bash
git clone https://github.com/retha01/casino-bonus-scraper.git
cd casino-bonus-scraper
```

Install the dependencies:

```bash
python -m pip install -r requirements.txt
```

Create a `.env` file in the project root and add:

```env
GEMINI_API_KEY=your_api_key_here
```

The API key is excluded from version control.

## Run the Scraper

Execute the following command:

```bash
python -m scraper.scrape
```

The scraper:

1. Checks the source website's robots.txt permissions.
2. Downloads the public comparison article.
3. Extracts the relevant casino bonus descriptions.
4. Uses Google Gemini to structure the extracted data.
5. Saves three records to `docs/bonuses.json`.

## Live Website

https://retha01.github.io/casino-bonus-scraper/

The webpage reads the generated JSON file and displays the casino
offers in a responsive comparison table.

To test locally:

```bash
python -m http.server 8000 --directory docs
```

Open http://localhost:8000 in your browser.

## Data Validation and Limitations

The information comes from a third-party comparison article and
may differ from the casino operators' latest offers.

Sports betting rollover requirements are not treated as casino
wagering requirements. Where the source does not establish a
casino wagering multiplier, the value is recorded as null.

The website displays the latest generated JSON file.
Scraper execution is currently manual rather than scheduled.

Gemini API access requires a valid API key and sufficient quota.

## Responsible Scraping

The scraper checks robots.txt and does not bypass
authentication, CAPTCHAs or website access restrictions.

## Additional Documentation

- [Production Scaling Plan](PRODUCTION_PLAN.md)
- [AI Usage](AI_USAGE.md)
- [Development Notes](NOTES.md)

## Development Time

Actual active development time: To be confirmed at completion.

The assessment is limited to three hours of active work.
Any incomplete requirements at the time limit will be disclosed
in the final submission.
