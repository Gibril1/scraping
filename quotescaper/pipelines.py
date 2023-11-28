# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter


class QuotescaperPipeline:
    def process_item(self, item, spider):

        adapter = ItemAdapter(item)

        # turn the tags from lists to comma separated strings
        tags = adapter.get('tags')
        string_representation = ', '.join(tags)
        adapter['tags'] = string_representation

        # strip all whitespaces from strings
        field_names = adapter.field_names()
        for field in field_names:
            value = adapter.get(field)
            adapter[field] = value.strip()

        return item
