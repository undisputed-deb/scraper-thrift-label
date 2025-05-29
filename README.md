# 🛍️ ThriftLabel Web Scraper with Scrapy + Playwright

This project is a robust web scraping pipeline built using [Scrapy](https://scrapy.org/) and [Playwright](https://playwright.dev/python/).  
It was designed to extract product data from **dynamic JavaScript-rendered websites**, particularly [ThriftLabel.com](https://thriftlabel.com).

---

## 🎯 Features

- 🔍 Scrapes product `title`, `price`, `URL`, and `image URL`
- 🌐 Supports multiple pages (pagination)
- 🧪 Tested on sample site `quotes.toscrape.com` for development
- 📊 Saves output directly to formatted Excel `.xlsx` file
- 🎨 Styled Excel output with bold headers, auto-width, and color

---

## 🛠️ Tech Stack

- Python 3.13  
- Scrapy 2.12  
- Playwright (headless Chromium browser)
- `openpyxl` (Excel formatting)
- PyCharm IDE  
- Git & GitHub for version control

---

## 📂 Project Structure

scrapy_company/
├── spiders/
│ ├── quotes_spider.py # Sample training spider
│ └── thriftlabel_spider.py # Main spider for ThriftLabel
├── pipelines.py # Excel writer logic
├── settings.py # Scrapy settings
├── items.py # (optional, not used here)
├── scrapy.cfg # Project config
page_debug.html # Rendered HTML snapshot (for debugging)
quotes.json # Sample output (training site)
quotes.xlsx # Sample output in Excel
thriftlabel_output.xlsx # Final output file


---

## 🧪 Phase 1: Training on QuotesToScrape

We began by building a basic Scrapy spider to scrape:
- Quote text
- Author name
- Tags

✅ The data was exported to JSON and Excel using a custom pipeline.

---

## 🚀 Phase 2: Scraping [ThriftLabel.com](https://thriftlabel.com)

We then applied the same structure to a real-world website:
- Used Playwright for JavaScript rendering
- Scraped:
  - `Title`
  - `Price`
  - `Product URL`
  - `Image URL`
- Scraped **3 pages** using paginated URLs
- Wrote output to `thriftlabel_output.xlsx` with headers, styles, and auto-fit columns

---

## 💾 Output Example (Excel)

| Title | Price | URL | Image URL |
|-------|-------|-----|-----------|
| Apple iPhone 14... | $319.99 | https://... | https://... |

---

## 📸 Screenshots (Optional)

> Add screenshots of:
> - Terminal output
> - Excel file opened
> - `page_debug.html` in browser
> - GitHub repo view

---

## ⚙️ How to Run This Project Locally

1. **Clone the repo**  
   ```bash
   git clone https://github.com/undisputed-deb/scraper-thrift-label.git
   cd scraper-thrift-label
python -m venv venv
venv\Scripts\activate  # On Windows
pip install -r requirements.txt
playwright install
scrapy crawl thriftlabel


📌 Author
Debashrestha Nandi
