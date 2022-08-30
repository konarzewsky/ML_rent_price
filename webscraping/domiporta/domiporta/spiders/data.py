import scrapy
import re


class Offer(scrapy.Item):
    url = scrapy.Field()##
    title = scrapy.Field()##
    price = scrapy.Field()##
    address = scrapy.Field()##
    parking = scrapy.Field()
    rooms = scrapy.Field()##
    floors = scrapy.Field()##
    building_type = scrapy.Field()##
    building_material = scrapy.Field()##
    kitchen = scrapy.Field()##
    size = scrapy.Field()##
    description = scrapy.Field()##
    features = scrapy.Field()##
    neighborhood = scrapy.Field()##
    year_built = scrapy.Field()##
    ownership = scrapy.Field()##
    latitude = scrapy.Field()##
    longitude = scrapy.Field()##



class LinksSpider(scrapy.Spider):
    name = 'apartments'
    allowed_domains = ['https://www.domiporta.pl/']
    try:
        with open("links.csv", "rt") as f:
            start_urls = ['https://www.domiporta.pl'+url.strip() for url in f.readlines()][1:]
    except:
        start_urls = []

    def parse(self, response):
        o = Offer() 

        
        title_xpath = '//span[@class="summary__subtitle-2"]/text()'#
        address_xpath = 'string(//span[@itemprop="address"])'#
        parking_xpath = '//p[text()="PARKING"]/following-sibling::*/text()'#
        price_xpath = '//span[@itemprop="price"]/@content'#
        rooms_xpath = '//p[text()="LICZBA POKOI"]/following-sibling::*/text()'#
        floors_xpath = '//p[text()="PIĘTRO"]/following-sibling::*/text()'#
        building_type_xpath = '//span[contains(text(),"Typ budynku")]/following-sibling::*/text()'#
        building_material_xpath = '//span[contains(text(),"Materiał")]/following-sibling::*/text()'#
        kitchen_xpath = '//span[contains(text(),"Kuchnia")]/following-sibling::*/text()'#
        size_xpath = '//p[text()="POWIERZCHNIA"]/following-sibling::*/text()'#
        neighborhood_xpath = '//dt[contains(text(),"Okolica:")]/following-sibling::*/text()'#
        description_xpath = '//div[@class="description__panel"]/text()'#
        features_xpath = '//dt[contains(text(),"Informacje dodatkowe:")]/following-sibling::*/text()'#
        year_built_xpath = '//span[contains(text(),"Rok budowy")]/following-sibling::*/text()'#
        ownership_xpath = '//span[contains(text(),"Forma własności")]/following-sibling::*/text()'#
        latitude_xpath = '//meta[@itemprop="latitude"]/@content'#
        longitude_xpath = '//meta[@itemprop="longitude"]/@content'#
        
        o['url'] = response.request.url
        o['title'] = response.xpath(title_xpath).getall()
        o['address'] = response.xpath(address_xpath).extract()
        o['parking'] = response.xpath(parking_xpath).extract()
        o['price'] = response.xpath(price_xpath).getall()
        o['rooms'] = response.xpath(rooms_xpath).getall()
        o['floors'] = response.xpath(floors_xpath).getall()
        o['building_type'] = response.xpath(building_type_xpath).getall()
        o['building_material'] = response.xpath(building_material_xpath).getall()
        o['kitchen'] = response.xpath(kitchen_xpath).getall()
        o['size'] = response.xpath(size_xpath).getall()
        o['neighborhood'] = response.xpath(neighborhood_xpath).getall()
        o['description'] = response.xpath(description_xpath).getall()
        o['features'] = response.xpath(features_xpath).getall()
        o['year_built'] = response.xpath(year_built_xpath).getall()
        o['ownership'] = response.xpath(ownership_xpath).getall()
        o['latitude'] = response.xpath(latitude_xpath).getall()
        o['longitude'] = response.xpath(longitude_xpath).getall()

        yield o
