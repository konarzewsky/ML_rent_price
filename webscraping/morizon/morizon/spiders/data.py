import scrapy
import re
import w3lib.html


class Offer(scrapy.Item):
    url = scrapy.Field()
    title = scrapy.Field()
    price = scrapy.Field()
    size = scrapy.Field()
    rooms = scrapy.Field()
    latitude = scrapy.Field()
    longitude = scrapy.Field()
     
    standard = scrapy.Field()
    floor = scrapy.Field()
    floors = scrapy.Field()
    balcony = scrapy.Field()
    windows = scrapy.Field()
    deposit = scrapy.Field()
    ownership = scrapy.Field()
    building_type = scrapy.Field()
    building_material = scrapy.Field()
    year_built = scrapy.Field()
    equipment = scrapy.Field()
    features = scrapy.Field()

    description = scrapy.Field()



class LinksSpider(scrapy.Spider):
    name = 'apartments'
    allowed_domains = ['https://www.morizon.pl/']
    try:
        with open("links2.csv", "rt") as f:
            start_urls = [url.strip() for url in f.readlines()][1:]
    except:
        start_urls = []

    def parse(self, response):
        o = Offer() 

        
        title_xpath = '//div[@class="col-xs-9"]/h1/strong/span/text()' ##
        price_xpath = '//li[@class="paramIconPrice"]/em/text()' ##
        size_xpath = '//li[@class="paramIconLivingArea"]/em/text()' ##
        rooms_xpath = '//li[@class="paramIconNumberOfRooms"]/em/text()' ##
        latitude_xpath = '//div[@id="property-map"]/@data-lat' ## 
        longitude_xpath = '//div[@id="property-map"]/@data-lng' ##
        standard_xpath = '//th[contains(text(),"Stan nieruchomości")]/following-sibling::*/text()' ##
        floor_xpath = '//th[contains(text(),"Piętro:")]/following-sibling::*/text()' ##
        floors_xpath = '//th[contains(text(),"Liczba pięter:")]/following-sibling::*/text()' ##
        balcony_xpath = '//th[contains(text(),"Balkon") or contains(text(),"balkon")]/following-sibling::*/text()' ##
        windows_xpath = '//th[contains(text(),"Stolarka okienna:")]/following-sibling::*/text()' ##
        deposit_xpath = '//th[contains(text(),"Depozyt za wynajem:")]/following-sibling::*/text()' ##
        ownership_xpath = '//th[contains(text(),"Forma własności:")]/following-sibling::*/text()' ##
        building_type_xpath = '//th[contains(text(),"Typ budynku")]/following-sibling::*/text()' ##
        building_material_xpath = '//th[contains(text(),"Materiał budowlany")]/following-sibling::*/text()' ##
        year_built_xpath = '//th[contains(text(),"Rok budowy")]/following-sibling::*/text()' ##
        features_xpath = '//h3[text()="Udogodnienia"]/following-sibling::*/text()' ##
        equipment_xpath = '//h3[text()="Wyposażenie"]/following-sibling::*/text()' ##

        # description_xpath = '//div[@class="description"]/p//text()'
        description_xpath = 'string(//div[@class="description"])'
        # description_xpath = '//div[@class="description"]/p/descendant-or-self::*/text()'
        
        o['url'] = response.request.url
        o['title'] = response.xpath(title_xpath).getall()
        o['price'] = response.xpath(price_xpath).getall()
        o['size'] = response.xpath(size_xpath).getall()
        o['rooms'] = response.xpath(rooms_xpath).getall()
        o['latitude'] = response.xpath(latitude_xpath).getall()
        o['longitude'] = response.xpath(longitude_xpath).getall()

        o['standard'] = response.xpath(standard_xpath).getall()
        o['floor'] = response.xpath(floor_xpath).getall()
        o['floors'] = response.xpath(floors_xpath).getall()
        o['balcony'] = response.xpath(balcony_xpath).getall()
        o['windows'] = response.xpath(windows_xpath).getall()
        o['deposit'] = response.xpath(deposit_xpath).getall()
        o['ownership'] = response.xpath(ownership_xpath).getall()
        o['building_type'] = response.xpath(building_type_xpath).getall()
        o['building_material'] = response.xpath(building_material_xpath).getall()
        o['year_built'] = response.xpath(year_built_xpath).getall()
        o['features'] = response.xpath(features_xpath).getall()
        o['equipment'] = response.xpath(equipment_xpath).getall()

        o['description'] = response.xpath(description_xpath).extract()
        # o['description'] = list(" ".join(response.xpath(description_xpath).extract()))

        yield o
