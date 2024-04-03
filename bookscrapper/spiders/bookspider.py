import os
from urllib.parse import urlencode
import scrapy
from bookscrapper.items import BookItem


class BookspiderSpider(scrapy.Spider):
    name = "bookspider"
    allowed_domains = ["books.toscrape.com", "proxy.scrapeops.io"]
    start_urls = ["https://books.toscrape.com"]
    path_to_file = os.path.join(os.path.dirname(
        os.path.abspath(__file__)), '..', '..', 'bookdata.csv')

    custom_settings = {
        'FEEDS': {
            path_to_file: {'format': 'csv', 'overwrite': True}
        }
    }

    # API_KEY = 'API_KEY'

    # def get_proxy_url(url):
    #     payload = {'api_key': API_KEY, 'url': url}
    #     proxy_url = 'https://proxy.scrapeops.io/v1/?' + urlencode(payload)
    #     return proxy_url
    
    # def start_requests(self) -> os.Iterable[scrapy.Request]:
    #     return scrapy.Request(url=get_proxy_url(self.start_urls[0]), callback=self.parse) 
    
    def parse_book_page(self, response):
        book = response.css("div.product_main")[0]
        table_rows = response.css("table tr")
        book_item = BookItem()

        book_item['url'] = response.url
        book_item['title'] = book.css("h1 ::text").get()
        book_item['upc'] = table_rows[0].css("td ::text").get()
        book_item['product_type'] = table_rows[1].css("td ::text").get()
        book_item['price_excl_tax'] = table_rows[2].css("td ::text").get()
        book_item['price_incl_tax'] = table_rows[3].css("td ::text").get()
        book_item['tax'] = table_rows[4].css("td ::text").get()
        book_item['availability'] = table_rows[5].css("td ::text").get()
        book_item['num_reviews'] = table_rows[6].css("td ::text").get()
        book_item['stars'] = book.css("p.star-rating").attrib['class']
        book_item['category'] = book.xpath(
            "//ul[@class='breadcrumb']/li[@class='active']/preceding-sibling::li[1]/a/text()").get()
        book_item['description'] = book.xpath(
            "//div[@id='product_description']/following-sibling::p/text()").get()
        book_item['price'] = book.css('p.price_color ::text').get()

        yield book_item

    def parse(self, response):
        books = response.css("article.product_pod")

        for book in books:
            book_link = book.css("h3 a::attr('href')").get()
            if "catalogue/" in book_link:
                book_link = book_link[10:]
            book_address = "https://books.toscrape.com/catalogue/" + book_link
            #meta={"proxy": "http://username:password@gate.smartproxy.com:7000"}
            #yield scrapy.Request(url=get_proxy_url(url), callback=self.parse)
            yield response.follow(book_address, callback=self.parse_book_page)

        next_page = response.xpath(
            "//li[@class='next']//a[contains(@href, 'page-')]//@href").get()

        if next_page is not None:
            if "catalogue/" in next_page:
                next_page = next_page[10:]
            next_page_url = "https://books.toscrape.com/catalogue/" + next_page
            #meta={"proxy": "http://username:password@gate.smartproxy.com:7000"}
            #yield scrapy.Request(url=get_proxy_url(url), callback=self.parse)
            yield response.follow(next_page_url, callback=self.parse)
