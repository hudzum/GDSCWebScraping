import scrapy

class BookScraper(scrapy.Spider):
    name = "book" 
    start_urls = ["https://books.toscrape.com/"] 

    def parse(self, response): 
           
            yield {
                'title': response.css('.h1 a::text').get() 
            }

