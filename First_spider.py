import scrapy

class BookScraper(scrapy.Spider):
    name = "book"  #This must be unique among 
    start_urls = ["https://books.toscrape.com/"] 

    def parse(self, response): 
           
            yield {
                'title': response.css('.h1 a::text').get() #CSS Selector for grabing the title!
            }

