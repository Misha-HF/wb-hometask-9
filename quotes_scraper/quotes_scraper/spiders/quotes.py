import scrapy
from ..items import QuoteItem

class QuotesSpider(scrapy.Spider):
    name = 'quotes_spider'
    start_urls = ['http://quotes.toscrape.com']

    def parse(self, response):
        for quote in response.xpath("//div[@class='quote']"):
            item = QuoteItem()
            item['quote'] = quote.xpath(".//span[@class='text']/text()").get()
            item['author'] = quote.xpath(".//span/small[@class='author']/text()").get()
            item['tags'] = quote.xpath(".//div[@class='tags']/a[@class='tag']/text()").getall()
            yield item

        next_page = response.xpath("//li[@class='next']/a/@href").get()
        if next_page:
            yield scrapy.Request(response.urljoin(next_page), callback=self.parse)

