# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy

class TagsProcessor(scrapy.Field):
    def input_processor(self, values):
        return values if isinstance(values, list) else [values]

class QuotescaperItem(scrapy.Item):
    quote_text = scrapy.Field()
    author = scrapy.Field()
    tags = TagsProcessor()
