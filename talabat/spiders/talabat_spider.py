import scrapy
import requests
import json

class Talabat(scrapy.Spider):
    name = 'talabat'
    start_urls = [
            'https://www.talabat.com/apiweb/v1/ksa/mostSellingItem',
            'https://www.talabat.com/apiweb/v1/bahrain/mostSellingItem',
            'https://www.talabat.com/apiweb/v1/uae/mostSellingItem',
            'https://www.talabat.com/apiweb/v1/oman/mostSellingItem',
            'https://www.talabat.com/apiweb/v1/kuwait/mostSellingItem',
            'https://www.talabat.com/apiweb/v1/qatar/mostSellingItem',
            'https://www.talabat.com/apiweb/v1/jordan/mostSellingItem',
            'https://www.talabat.com/apiweb/v1/egypt/mostSellingItem',
            'https://www.talabat.com/apiweb/v1/iraq/mostSellingItem',
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
        out_list = []
        for url in urls:
            res = requests.get(url[1])
            out_list.append(res.json)
        json_file = open('out.json','w')
        json.dump(json.dumps(out_list),json_file)
        json_file.close()


''' for i in urls:
    resp = requests.get(url=i[1])
    data = resp.json()

    with open(i[0] + ".json", "w") as outfile:
        outfile.write(data)



params = dict(
    origin='Chicago,IL',
    destination='Los+Angeles,CA',
    waypoints='Joplin,MO|Oklahoma+City,OK',
    sensor='false'
)


resp = requests.get(url=url, params=params)
data = resp.json()

with open("sample.json", "w") as outfile:
    outfile.write(json_object)
 '''