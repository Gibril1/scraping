import scrapy
from quotescaper.items import QuotescaperItem

class QuotespiderSpider(scrapy.Spider):
    name = "quotespider"
    allowed_domains = ["quotes.toscrape.com"]
    start_urls = ["https://quotes.toscrape.com/"]

    def parse(self, response):
        scraped_quotes = QuotescaperItem()
        all_quotes = response.css(".col-md-8 .quote")
        for quote in all_quotes:
            scraped_quotes['quote_text'] = quote.css(".text ::text").get()
            scraped_quotes['author'] = quote.css(".author::text").get()
            scraped_quotes['tags'] = quote.css(".tags a::text").getall()
            
            yield scraped_quotes
        
        next_page = response.css('li.next a ::attr(href)').get()

        if next_page is not None:
            next_page_url = "https://quotes.toscrape.com/" + next_page

            yield response.follow(next_page_url, callback=self.parse)