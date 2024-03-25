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

import json

class QuotesJsonPipeline:
    def open_spider(self, spider):
        if spider.name == 'quotes_spider':
            self.quotes_data = []

    def close_spider(self, spider):
        # Зберігаємо дані про цитати у JSON файл
        if spider.name == 'quotes_spider':
            with open('quotes.json', 'w') as f:
                json.dump(self.quotes_data, f, indent=4)

    def process_item(self, item, spider):
        # Перевіряємо, чи поточний спайдер quotes_spider
        if spider.name == 'quotes_spider':
            # Додаємо дані про цитати до списку
            self.quotes_data.append(dict(item))
        return item

class AuthorsJsonPipeline:
    def open_spider(self, spider):
        # Перевіряємо, чи поточний спайдер не є quotes_spider
        if spider.name == 'authors_spider':
            self.authors_data = []

    def close_spider(self, spider):
        # Зберігаємо дані про авторів у JSON файл лише у випадку, якщо поточний спайдер не є quotes_spider
        if spider.name == 'authors_spider':
            with open('authors.json', 'w') as f:
                json.dump(self.authors_data, f, indent=4)

    def process_item(self, item, spider):
        # Перевіряємо, чи поточний спайдер не є quotes_spider
        if spider.name == 'authors_spider' and all(item.values()):
            # Перевіряємо, чи автор ще не існує в списку authors_data
            if not any(author['fullname'] == item['fullname'] for author in self.authors_data):
                # Додаємо дані про авторів до списку
                self.authors_data.append(dict(item))
        return item
