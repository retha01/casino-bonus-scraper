
# AI Usage

1. I used Claude and ChatGPT to assist with planning, implementing, debugging and documenting the application.
2. I first used anthropic and my credits were finished, switched to google gemini and i had to use a different version as the one i was on 2.53 was outdated and 3.1 was being used by a lot of people and gave a 503 error, once i found the best version it was integrated into the Python scraper to convert unstructured casino bonus descriptions into structured JSON data.
3. During testing, Gemini incorrectly interpreted Bettabets' 8x sports rollover requirement as a casino wagering multiplier.
4. I identified the issue by comparing the extracted output with the source conditions and updated the extraction instructions to distinguish sports wagering from casino wagering.
5. After rerunning the scraper, Gemini correctly returned null for the unsupported casino wagering multiplier, and the updated JSON was successfully generated.
