import scrapy
import re


class Offer(scrapy.Item):
    url = scrapy.Field()#
    title = scrapy.Field()#
    price = scrapy.Field()#
    address = scrapy.Field()#
    floors = scrapy.Field()#
    rooms = scrapy.Field()#
    floor = scrapy.Field()#
    building_type = scrapy.Field()#
    year_built = scrapy.Field()#
    size = scrapy.Field()#
    description = scrapy.Field()#
    features = scrapy.Field()#
    latitude = scrapy.Field()#
    longitude = scrapy.Field()#
    building_material = scrapy.Field()#
    kitchen = scrapy.Field()#
    standard = scrapy.Field()#
    parking = scrapy.Field()#



class LinksSpider(scrapy.Spider):
    name = 'apartments'
    allowed_domains = ['https://www.gratka.pl/']
    user_agent = "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/22.0.1207.1 Safari/537.1"
    try:
        with open("links.csv", "rt") as f:
            start_urls = [url.strip() for url in f.readlines()][1:]
    except:
        start_urls = []

    def parse(self, response):
        o = Offer() 

        
        title_xpath = '//h1[@class="sticker__title"]/text()'###
        address_xpath = 'string(//span[@class="offerLocation"])'###
        price_xpath = '//span[@class="priceInfo__value"]/text()'###
        rooms_xpath = '//span[contains(text(),"Liczba pokoi")]/following-sibling::*/text()'###
        floor_xpath = '//span[contains(text(),"Piętro")]/following-sibling::*/text()'###
        floors_xpath = '//span[contains(text(),"Liczba pięter w budynku")]/following-sibling::*/text()'###
        year_built_xpath = '//span[contains(text(),"Rok budowy")]/following-sibling::*/text()'###
        building_type_xpath = '//span[contains(text(),"Typ zabudowy")]/following-sibling::*/text()'###
        features_xpath = 'string(//ul[@class="parameters__groupedParameters"])'###
        size_xpath = '//span[contains(text(),"Powierzchnia w m2")]/following-sibling::*/text()'###
        location_xpath = "//script[contains(., 'latitude')]/text()"###
        description_xpath = 'string(//div[@class="description__rolled ql-container"])'###
        building_material_xpath = '//span[contains(text(),"Materiał budynku")]/following-sibling::*/text()'###
        parking_xpath = '//span[contains(text(),"Liczba miejsc parkingowych")]/following-sibling::*/text()'###
        kitchen_xpath = '//span[contains(text(),"Forma kuchni")]/following-sibling::*/text()'###
        standard_xpath = '//span[contains(text(),"Stan")]/following-sibling::*/text()'###

        o['url'] = response.request.url
        o['title'] = response.xpath(title_xpath).getall()
        o['address'] = response.xpath(address_xpath).extract()
        o['price'] = response.xpath(price_xpath).getall()
        o['rooms'] = response.xpath(rooms_xpath).getall()
        o['floor'] = response.xpath(floor_xpath).getall()
        o['floors'] = response.xpath(floors_xpath).getall()
        o['year_built'] = response.xpath(year_built_xpath).getall()
        o['building_type'] = response.xpath(building_type_xpath).getall()
        o['features'] = response.xpath(features_xpath).extract()
        o['size'] = response.xpath(size_xpath).getall()
        o['latitude'] = eval(response.xpath(location_xpath).getall()[0]).get('@graph')[0].get('geo').get('latitude')
        o['longitude'] = eval(response.xpath(location_xpath).getall()[0]).get('@graph')[0].get('geo').get('longitude')
        o['description'] = response.xpath(description_xpath).extract()
        o['building_material'] = response.xpath(building_material_xpath).getall()
        o['kitchen'] = response.xpath(kitchen_xpath).getall()
        o['standard'] = response.xpath(standard_xpath).getall()
        o['parking'] = response.xpath(parking_xpath).getall()

        yield o
