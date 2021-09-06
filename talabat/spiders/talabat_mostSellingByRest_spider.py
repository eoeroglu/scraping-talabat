import scrapy
import json

class Talabat_MSBR(scrapy.Spider):
    name = 'talabat_mostSellingByRest'

    start_urls = [
        'https://www.talabat.com/apiweb/v1/ksa/mostSellingByRest/0',
        'https://www.talabat.com/apiweb/v1/kuwait/mostSellingByRest/0',
        'https://www.talabat.com/apiweb/v1/bahrain/mostSellingByRest/0',
        'https://www.talabat.com/apiweb/v1/uae/mostSellingByRest/0',
        'https://www.talabat.com/apiweb/v1/oman/mostSellingByRest/0',
        'https://www.talabat.com/apiweb/v1/qatar/mostSellingByRest/0',
        'https://www.talabat.com/apiweb/v1/jordan/mostSellingByRest/0',
        'https://www.talabat.com/apiweb/v1/egypt/mostSellingByRest/0',
        'https://www.talabat.com/apiweb/v1/iraq/mostSellingByRest/0'
    ]

    def parse(self, response):
        jres = json.loads(response.text)
        for item in jres['result']['mostSellingItemsRestaurant']:
            yield {
                'id': item['id'],
                'name': item['rna'],
                'cuisine': item['cs']
            }