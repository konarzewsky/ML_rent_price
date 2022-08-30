import scrapy
from urllib import request
from bs4 import BeautifulSoup as BS
import re

cities = {
    'warszawa':272,
    'krakow':100,
    'poznan':42,
    'wroclaw':47,
    'gdansk':35,
    'gdynia':16,
    'szczecin':24,
    'bialystok':12,
    'katowice':36,
    'lublin':18,
    'lodz':39,
    'bydgoszcz':22,
}

def url(city):
    return f"https://www.otodom.pl/pl/oferty/wynajem/mieszkanie/{city}?page="

# first_url = url("warszawa") + "1"
# html = request.urlopen(first_url)
# bs = BS(html.read(), 'html.parser')
# last_page = int(bs.find_all('a', {'href':re.compile('https:\/\/www.otomoto\.pl/osobowe\/opel\/astra\/\?search%5Border%5D=created_at%3Adesc&page=[0-9]{1,3}')})[-2].span.text)
# last_page =350


class Link(scrapy.Item):
    link = scrapy.Field()

class LinksSpider(scrapy.Spider):
    name = 'offers'
    allowed_domains = ['https://www.otodom.pl/']

    start_urls = []
    for city in cities.keys():
        for i in range(cities[city]):
            start_urls.append(url(city)+str(i))
    print(start_urls)
    def parse(self, response):

        offer_xpath = '//a[@data-cy="listing-item-link"]/@href'
        # offer_xpath = '//a[@class="css-19ukcmm es62z2j29"]/@href'
        selection = response.xpath(offer_xpath)
        for s in selection:
            l = Link()
            l['link'] = s.get()
            yield l
