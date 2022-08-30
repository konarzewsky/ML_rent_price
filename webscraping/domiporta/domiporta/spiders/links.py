import scrapy
from urllib import request
from bs4 import BeautifulSoup as BS
import re

cities = {
    'mazowieckie/warszawa':280,
    'malopolskie/krakow':41,
    'wielkopolskie/poznan':10,
    'dolnoslaskie/wroclaw':17,
    'pomorskie/gdansk':11,
    'pomorskie/gdynia':6,
    'zachodniopomorskie/szczecin':8,
    'podlaskie/bialystok':4,
    'slaskie/katowice':12,
    'lubelskie/lublin':5,
    'lodzkie/lodz':10,
    'kujawsko-pomorskie/bydgoszcz':8,
}

def url(city):
    return f"https://www.domiporta.pl/mieszkanie/wynajme/{city}?PageNumber="



class Link(scrapy.Item):
    link = scrapy.Field()

class LinksSpider(scrapy.Spider):
    name = 'offers'
    allowed_domains = ['https://www.domiporta.pl/']

    start_urls = []
    for city in cities.keys():
        for i in range(cities[city]):
            start_urls.append(url(city)+str(i))

    def parse(self, response):

        offer_xpath = '//article[@class="sneakpeak"]/@data-href'
        selection = response.xpath(offer_xpath)
        for s in selection:
            l = Link()
            l['link'] = s.get()
            yield l
