import scrapy
#import requests
import json

class Talabat_MSI(scrapy.Spider):
    name = 'talabat_mostSellingItems'
    start_urls = [
            'https://www.talabat.com/apiweb/v1/ksa/mostSellingItem',
            'https://www.talabat.com/apiweb/v1/bahrain/mostSellingItem',
            'https://www.talabat.com/apiweb/v1/uae/mostSellingItem',
            'https://www.talabat.com/apiweb/v1/oman/mostSellingItem',
            'https://www.talabat.com/apiweb/v1/kuwait/mostSellingItem',
            'https://www.talabat.com/apiweb/v1/qatar/mostSellingItem',
            'https://www.talabat.com/apiweb/v1/jordan/mostSellingItem',
            'https://www.talabat.com/apiweb/v1/egypt/mostSellingItem',
            'https://www.talabat.com/apiweb/v1/iraq/mostSellingItem'
        ]
    def parse(self, response):
        jres = json.loads(response.text)
        for item in jres['result']['mostSellingItems']:
            yield {
                'id': item['id'],
                'name': item['na'],
                'rid': item['rid'],
                'restaurant': item['rna'],
                'desc': item['dsc'],
                'slg': item['slg']
            }


''' for i in urls:
    resp = requests.get(url=i[1])
    data = resp.json()

    with open(i[0] + ".json", "w") as outfile:
        outfile.write(data)

out_list = []
for url in urls:
    res = requests.get(url[1])
    out_list.append(res.json)
json_file = open('out.json','w')
json.dump(json.dumps(out_list),json_file)
json_file.close()

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