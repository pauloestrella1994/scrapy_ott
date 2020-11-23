import scrapy


class MercadoLivreSpider(scrapy.Spider):
    name = "mercado_livre"

    start_urls = ['https://lista.mercadolivre.com.br/olist#D[A:olist]']

        
    def parse(self, response):
        product_name = response.css('.ui-search-item__title::text').getall()
        prices = response.xpath('//div[has-class("ui-search-price--size-medium")]' +
                                '//span[has-class("price-tag ui-search-price__part")]' + 
                                '//span[has-class("price-tag-fraction")]/text()').getall()
        yield {
            'product_name': product_name,
            'price': prices
        }

