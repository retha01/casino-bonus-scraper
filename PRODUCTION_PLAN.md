
# Production Scaling Plan

## Scaling to 200 Casinos

To scale this project to 200 casinos with daily updates, I would deploy
the Python scraper on a small Linux VPS hosted by Hetzner or DigitalOcean.
I would use Docker to package the application and its dependencies,
making deployment and maintenance easier.

For data storage, I would use PostgreSQL to maintain casino information,
bonus offers, source URLs, extraction dates and historical changes.
Automated daily database backups would be saved to separate cloud
object storage, with periodic restoration testing.

I would schedule daily scraping using cron initially. The application
would process permitted sources in controlled batches, respecting
robots.txt and rate limits. Failed requests would be retried with
exponential backoff. Gemini would extract structured information from
new or changed bonus text, while validation rules would identify
missing values and unusual changes for manual review.

I would use FastAPI for the backend and a lightweight HTML,
CSS and JavaScript frontend. Cloudflare would handle DNS, while
Nginx and Let's Encrypt would provide HTTPS and reverse-proxy
functionality.

For monitoring, I would log scraper executions, record failed
extractions and track when each casino was last updated.
Email alerts would notify me when a scheduled run fails or
important data becomes outdated.

An indicative monthly budget would be $25-$60, covering
approximately $10-$20 for hosting, $5-$10 for backups and
storage, and $10-$30 for AI processing and monitoring.
These are preliminary estimates excluding development labour.
Actual costs would depend on API usage, traffic and the
complexity of the target websites.

I would initially keep the architecture simple and only
introduce separate workers, queues and additional servers
when traffic or scraping volume justifies the complexity.
