# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html

# useful for handling different item types with a single interface

from itemadapter import ItemAdapter
from models import Quote, Author
import connect

class QuotesMongoDBPipeline:
    def process_item(self, item, spider):
        adapter = ItemAdapter(item)
        if 'quote' in adapter and 'author' in adapter and 'tags' in adapter:
            quote = Quote(
                quote=adapter['quote'],
                author=adapter['author'],
                tags=adapter['tags']
            )
            quote.save()
        return item

class AuthorsMongoDBPipeline:
    def process_item(self, item, spider):
        adapter = ItemAdapter(item)
        if 'fullname' in adapter and 'born_date' in adapter and 'born_location' in adapter and 'description' in adapter:
            author = Author(
                fullname=adapter['fullname'],
                born_date=adapter['born_date'],
                born_location=adapter['born_location'],
                description=adapter['description']
            )
            author.save()
        return item
