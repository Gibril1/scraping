import scrapy


class QuotespiderSpider(scrapy.Spider):
    name = "quotespider"
    allowed_domains = ["quotes.toscrape.com"]
    start_urls = ["https://quotes.toscrape.com/"]

    def parse(self, response):
        all_quotes = response.css(".col-md-8 .quote")
        for quote in all_quotes:
            yield{
                'quote_text': quote.css(".text ::text").get(),
                'author': quote.css(".author::text").get(),
                'tags': quote.css(".tags a::text").getall(),
            }
