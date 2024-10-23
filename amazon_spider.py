import scrapy

class AmazonSpider(scrapy.Spider):
    name = "amazon"
    start_urls = ['https://www.amazon.com/s?bbn=679255011&rh=n%3A679255011%2Cp_85%3A2470955011&pf_rd_i=7147441011&pf_rd_m=ATVPDKIKX0DER&pf_rd_p=722949b4-757d-4d03-aad7-04d950c471f2&pf_rd_r=X2D7FDG0K6NM9XRNXEJY&pf_rd_s=merchandised-search-3&ref=win24_ml1_mob_nav_2']

    def parse(self, response):
        for listing in response.css('.gsx-ies-anchor .sg-col-inner'):

            yield {
                'title': listing.css('.a-color-base.a-text-normal::text').get(),
            }
