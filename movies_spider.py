import scrapy

class MoviesSpider(scrapy.Spider):
    name = "movies"
    start_urls = ['https://www.rottentomatoes.com/browse/movies_in_theaters/sort:top_box_office']

    def parse(self, response):
        for movie in response.css('#main-page-content a'):

            yield {
                'title': movie.css('.p--small::text').get(),
                'critics_score' : movie.css('score-icon-critics + rt-text::text').get(),
                'audience_score' : movie.css('score-icon-audience + rt-text::text').get()
            }
