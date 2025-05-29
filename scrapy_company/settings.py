# Scrapy settings for scrapy_company project

BOT_NAME = "scrapy_company"

SPIDER_MODULES = ["scrapy_company.spiders"]
NEWSPIDER_MODULE = "scrapy_company.spiders"

# Obey robots.txt rules
ROBOTSTXT_OBEY = False

# Configure item pipelines
ITEM_PIPELINES = {
    "scrapy_company.pipelines.ScrapyCompanyPipeline": 300,
}

# ✅ Enable Scrapy Playwright integration
DOWNLOAD_HANDLERS = {
    "http": "scrapy_playwright.handler.ScrapyPlaywrightDownloadHandler",
    "https": "scrapy_playwright.handler.ScrapyPlaywrightDownloadHandler",
}

TWISTED_REACTOR = "twisted.internet.asyncioreactor.AsyncioSelectorReactor"
FEED_EXPORT_ENCODING = "utf-8"

# Optional: headless browser, can set headless=False for debugging
PLAYWRIGHT_BROWSER_TYPE = "chromium"
PLAYWRIGHT_LAUNCH_OPTIONS = {"headless": True}

# Optional: timeout settings
# PLAYWRIGHT_DEFAULT_NAVIGATION_TIMEOUT = 30 * 1000  # 30 seconds
