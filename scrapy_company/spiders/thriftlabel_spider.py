import scrapy
from scrapy_playwright.page import PageMethod

class ThriftlabelSpider(scrapy.Spider):
    name = "thriftlabel"

    def start_requests(self):
        search_term = "Iphone 14"
        for page in range(1, 4):  # Pages 1, 2, 3
            url = f"https://thriftlabel.com/search/?q={search_term.replace(' ', '+')}&page={page}"
            yield scrapy.Request(
                url,
                meta={
                    "playwright": True,
                    "playwright_page_methods": [
                        PageMethod("wait_for_timeout", 2000)
                    ]
                },
                callback=self.parse
            )

    def parse(self, response):
        print("✅ PAGE LOADED LENGTH:", len(response.text))

        for product in response.css("div.col-6.col-md-4.col-lg-3.col-xl-5-custom"):
            title = product.css("h6::text").get(default="N/A").strip()
            price = product.css("p.fw-bold::text").get(default="N/A").strip()
            url = response.urljoin(product.css("a::attr(href)").get(default=""))

            yield {
                "title": title,
                "price": price,
                "url": url
            }

