import scrapy
import re
import json

class Offer(scrapy.Item):
    url = scrapy.Field()
    title = scrapy.Field()
    price = scrapy.Field()
    address = scrapy.Field()
    rent = scrapy.Field()
    rooms = scrapy.Field()
    floor = scrapy.Field()
    floors = scrapy.Field()
    heating = scrapy.Field()
    year_built = scrapy.Field()
    deposit = scrapy.Field()
    building_type = scrapy.Field()
    building_material = scrapy.Field()
    status = scrapy.Field()
    size = scrapy.Field()
    windows = scrapy.Field()
    description = scrapy.Field()
    features = scrapy.Field()
    latitude = scrapy.Field()
    longitude = scrapy.Field()



class LinksSpider(scrapy.Spider):
    name = 'apartments'
    allowed_domains = ['https://www.otodom.pl/']
    user_agent = "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/22.0.1207.1 Safari/537.1"
    try:
        with open("links.csv", "rt") as f:
            start_urls = ['https://www.otodom.pl'+url.strip() for url in f.readlines()]
    except:
        start_urls = []

    def parse(self, response):
        o = Offer() 

        
        title_xpath = '//h1[@class="css-1hsbwdh eu6swcv17"]/text()'
        address_xpath = '//a[@class="css-1ibwe9h e1nbpvi62"]/text()'
        price_xpath = '//strong[@class="css-srd1q3 eu6swcv16"]/text()'
        rent_xpath = '//div[@title="Czynsz - dodatkowo"]/following-sibling::*/div/text()'
        rooms_xpath = '//div[@title="Liczba pokoi"]/following-sibling::*/@title'
        floor_xpath = '//div[@title="Piętro"]/following-sibling::*/@title'
        floors_xpath = '//div[@title="Liczba pięter"]/following-sibling::*/@title'
        heating_xpath = '//div[@title="Ogrzewanie"]/following-sibling::*/@title'
        year_built_xpath = '//div[@title="Rok budowy"]/following-sibling::*/@title'
        deposit_xpath = '//div[@title="Kaucja"]/following-sibling::*/@title'
        building_type_xpath = '//div[@title="Rodzaj zabudowy"]/following-sibling::*/@title'
        building_material_xpath = '//div[@title="Materiał budynku"]/following-sibling::*/@title'
        status_xpath = '//div[@title="Stan wykończenia"]/following-sibling::*/@title'
        size_xpath = '//div[@title="Powierzchnia"]/following-sibling::*/@title'
        windows_xpath = '//div[@title="Okna"]/following-sibling::*/@title'
        description_xpath = '//div[@data-cy="adPageAdDescription"]/p/text()'
        features_xpath = '//li[@data-cy="ad.ad-features.categorized-list.item-with-category"]/text()'
        coordinates_xpath = "//script[contains(., 'latitude')]/text()" ## tylko to nie jest zrobione
        
        o['url'] = response.request.url
        o['title'] = response.xpath(title_xpath).getall()
        o['price'] = response.xpath(price_xpath).getall()
        o['address'] = response.xpath(address_xpath).getall()
        o['rent'] = response.xpath(rent_xpath).getall()
        o['rooms'] = response.xpath(rooms_xpath).getall()
        o['floor'] = response.xpath(floor_xpath).getall()
        o['floors'] = response.xpath(floors_xpath).getall()
        o['heating'] = response.xpath(heating_xpath).getall()
        o['year_built'] = response.xpath(year_built_xpath).getall()
        o['deposit'] = response.xpath(deposit_xpath).getall()
        o['building_type'] = response.xpath(building_type_xpath).getall()
        o['building_material'] = response.xpath(building_material_xpath).getall()
        o['status'] = response.xpath(status_xpath).getall()
        o['size'] = response.xpath(size_xpath).getall()
        o['windows'] = response.xpath(windows_xpath).getall()
        o['description'] = response.xpath(description_xpath).getall()
        o['features'] = response.xpath(features_xpath).getall()
        o['latitude'] = json.loads(response.xpath(coordinates_xpath).getall()[0])["props"]["pageProps"]["ad"]["location"]["coordinates"]["latitude"]
        o['longitude'] = json.loads(response.xpath(coordinates_xpath).getall()[0])["props"]["pageProps"]["ad"]["location"]["coordinates"]["longitude"]

        yield o
