import scrapy
from urllib import request
from bs4 import BeautifulSoup as BS
import re

cities = {
    'warszawa':195,
    'krakow':72,
    'poznan':20,
    'wroclaw':25,
    'gdansk':17,
    'gdynia':9,
    'szczecin':10,
    'bialystok':5,
    'katowice':23,
    'lublin':8,
    'lodz':28,
    'bydgoszcz':10,
}

def url(city):
    return f"https://gratka.pl/nieruchomosci/mieszkania/{city}/wynajem?page="



class Link(scrapy.Item):
    link = scrapy.Field()

class LinksSpider(scrapy.Spider):
    name = 'offers'
    allowed_domains = ['https://www.gratka.pl/']
    user_agent = "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/22.0.1207.1 Safari/537.1"
    start_urls = []
    for city in cities.keys():
        for i in range(cities[city]):
            start_urls.append(url(city)+str(i))

    def parse(self, response):

        # offer_xpath = '//a[@data-cy="listing-item-link"]/@href'
        offer_xpath = '//article[contains(@class, "teaserUnified")]/@data-href'
        selection = response.xpath(offer_xpath)
        for s in selection:
            l = Link()
            l['link'] = s.get()
            yield l
