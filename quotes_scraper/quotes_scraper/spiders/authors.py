import scrapy
from ..items import AuthorItem

class AuthorsSpider(scrapy.Spider):
    name = 'authors_spider'
    start_urls = ['http://quotes.toscrape.com']

    def parse(self, response):
        author_links = response.xpath("//span/a/@href").getall()
        for author_link in author_links:
            yield scrapy.Request(response.urljoin(author_link), callback=self.parse_author)

        next_page = response.xpath("//li[@class='next']/a/@href").get()
        if next_page:
            yield scrapy.Request(response.urljoin(next_page), callback=self.parse)

    def parse_author(self, response):
        item = AuthorItem()
        item['fullname'] = response.xpath("//h3[@class='author-title']/text()").get()
        item['born_date'] = response.xpath("//span[@class='author-born-date']/text()").get()
        item['born_location'] = response.xpath("//span[@class='author-born-location']/text()").get()
        item['description'] = response.xpath("//div[@class='author-description']/text()").get()
        yield item
