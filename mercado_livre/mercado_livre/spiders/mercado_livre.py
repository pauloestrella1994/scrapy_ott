import scrapy


class MercadoLivreSpider(scrapy.Spider):
    name = "mercado_livre"

    def requests_pages(self):
        urls = [
            'https://lista.mercadolivre.com.br/olist',
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)
        
    def parse(self, response):
        product_name = quote.css('.ui-search-item__title::text').getall()
        prices = quote.xpath('//div[has-class("ui-search-price--size-medium")]//span[has-class("price-tag ui-search-price__part")]//span[has-class("price-tag-fraction")]/text()').getall()

        for quote in response:
            yield {
                'product_name': product_name,
                'price': prices,
            }
