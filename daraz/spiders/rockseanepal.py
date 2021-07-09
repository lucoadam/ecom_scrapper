# -*- coding: utf-8 -*-
import scrapy
from scrapy import Request
from scrapy.spiders import Rule
import time


def unique(list1):

    # intilize a null list
    unique_list = []

    # traverse for all elements
    for x in list1:
        # check if exists in unique_list or not
        if x not in unique_list:
            unique_list.append(x)
    # print list
    return unique_list

class RockSeaNepalSpider(scrapy.Spider):
    name = 'rockseanepal'
    allowed_domains = ['daraz.com.np']

    start_urls = ['https://cheers.com.np/category?c=whisky', 'https://cheers.com.np/category?c=vodka', 'https://cheers.com.np/category?c=gin', 'https://cheers.com.np/category?c=rum', 'https://cheers.com.np/category?c=brandy', 'https://cheers.com.np/category?c=liqueur', 'https://cheers.com.np/category?c=tequila', 'https://cheers.com.np/category?c=wine', 'https://cheers.com.np/category?c=beer', 'https://cheers.com.np/category?c=japanese-liquor', 'https://cheers.com.np/category?c=beverages', 'https://cheers.com.np/category?c=glass', 'https://cheers.com.np/category?c=mixers', 'https://cheers.com.np/category?c=snacks', 'https://cheers.com.np/category?c=offers']
    # start_urls = [
    #  "https://cheers.com.np/"
    #  # "http://rockseanepal.com/shop/page/2/"
    #  # "http://rockseanepal.com/shop/page/3/"
    #  # "http://rockseanepal.com/shop/page/4/"
    #  # "http://rockseanepal.com/shop/page/5/"
    #  # "http://rockseanepal.com/shop/page/6/"
    #  # "http://rockseanepal.com/shop/page/7/"
    #  # "http://rockseanepal.com/shop/page/8/"
    #  # "http://rockseanepal.com/shop/page/9/"
    #  # "http://rockseanepal.com/shop/page/10/"
    #  # "http://rockseanepal.com/shop/page/11/"
    # ]


    def parse(self, response):
        # links1= response.xpath("//div[@class='sku -gallery -validate-size ']/a[@class='link']/@href").extract()
        # links2= response.xpath("//div[@class='sku -gallery ']/a[@class='link']/@href").extract()
        self.logger.info('A response from %s just arrived!', response.url)
        links = response.xpath('//div[@id="productList"]/div/a[@class="container-link"]/@href').extract()
        links = unique(links)
        for link in links:
            yield Request('https://cheers.com.np'+link, callback=self.parse_article, dont_filter=True)
        # for link in links:
        #     import json
        #     link = json.loads(link)
        #     print(link['name'])
        #     # yield {
        #     #     "Type": "simple",
        #     #     "SKU": link['sku'],
        #     #     'Name': link['name'],
        #     #     "Published":1,
        #     #     "Is featured?":1,
        #     #     "Visibility in catalog": "visible",
        #     #     "Short description": "This is product description",
        #     #     "Description":link['description'],
        #     #     "Date sale price starts":"",
        #     #     "Date sale price ends":"",
        #     #     "Tax status":"taxable",
        #     #     "Tax class":"",
        #     #     "In stock?":1,
        #     #     "Stock": 100,
        #     #     "Allow customer reviews?":1,
        #     #     "Categories": "> ".join([cat['name'] for cat in link['categories']]),
        #     #     'Regular price': int(link['price'])*1.12,
        #     #     'Sale price': int(link['price']),
        #     #     "Images": ",".join(['https://www.reddoko.com/uploads/'+str(image['media_id'])+'/'+image['file'] for image in link['images']])
        #     # }
        #
        # # links= links1 + links2
        # # self.logger.info(links)
        # for link in links:
        #     if '/item/' in link:
        #         print(link)
                # time.sleep(2)

                # yield Request(link, callback=self.parse_article, dont_filter=True)
        #
        # nextpageurl = response.xpath('//li/a[@title="Next"]/@href').extract_first()
        # absolute_next_page_url = response.urljoin(nextpageurl)
        # yield scrapy.Request(nextpageurl, dont_filter=True)

    def parse_article(self, response):
        title = response.xpath("//h4/text()").extract_first()
        price = response.xpath("//h3/text()").extract_first()
        price = "".join(price.split()[1].split(','))
        # price = [int(s) for s in price.split() if s.isdigit()]
        description = response.xpath('//div[@class="description"]').extract()
        short_description = response.xpath('//div[@class="description"]/p/text()').extract_first()
        category = response.xpath("//div[@id='main']/ul/li/a/text()").extract()[:-1]
        seller = ""

        images = ['https://cheers.com.np'+img for img in response.xpath("//img[@title='"+title+"']/@data-original").extract()]

        yield {
            "ID":"",
            "Type": "simple",
            "SKU": "-".join(title.lower().split()),
            'Name': title,
            "Published":1,
            "Is featured?":1,
            "Visibility in catalog": "visible",
            "Short description": short_description,
            "Description": description,
            "Date sale price starts":"",
            "Date sale price ends":"",
            "Tax status":"taxable",
            "Tax class":"",
            "In stock?":1,
            "Stock": 100,
            "Allow customer reviews?":1,
            "Categories": " > ".join(category),
            'Regular price': int("".join(("".join(price.split("Rs"))).split()))*1.12,
            'Sale price': int("".join(("".join(price.split("Rs"))).split())),
            # 'Regular price': int("".join(("".join(price.split("Rs"))).split()))*1.12,
            # 'Sale price': int("".join(("".join(price.split("Rs"))).split())),
            "Images": ",".join(images)

        }

