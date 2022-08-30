import scrapy
from urllib import request
from bs4 import BeautifulSoup as BS
import re

cities = {
    'warszawa':175,
    'krakow':70,
    'poznan':17,
    'wroclaw':21,
    'gdansk':17,
    'gdynia':7,
    'szczecin':10,
    'bialystok':3,
    'katowice':19,
    'lublin':7,
    'lodz':24,
    'bydgoszcz':12,
}

def url(city):
    return f"https://www.morizon.pl/do-wynajecia/mieszkania/{city}/?page="

# first_url = url + "1"
# html = request.urlopen(first_url)
# bs = BS(html.read(), 'html.parser')


class Link(scrapy.Item):
    link = scrapy.Field()

class LinksSpider(scrapy.Spider):
    name = 'offers'
    allowed_domains = ['https://www.morizon.pl/']

    start_urls = []
    for city in cities.keys():
        for i in range(cities[city]):
            start_urls.append(url(city)+str(i))

    def parse(self, response):

        offer_xpath = '//a[@class="property_link property-url"]/@href'
        selection = response.xpath(offer_xpath)
        for s in selection:
            l = Link()
            l['link'] = s.get()
            yield l
