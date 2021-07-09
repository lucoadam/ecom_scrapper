# -*- coding: utf-8 -*-
import scrapy
from scrapy import Request
from scrapy.spiders import Rule
import time

class DarazallSpider(scrapy.Spider):
    name = 'darazall'
    allowed_domains = ['daraz.com.np']


    # start_urls = [
    #     "https://www.daraz.com.np/smartphones/",
    #     "https://www.daraz.com.np/smartphones/samsung-brand/?spm=a2a0e.searchlistcategory.cate_1_1.1.2adc3056U88ocZ",
    #     "https://www.daraz.com.np/smartphones/oneplus_brand/",
    #     "https://www.daraz.com.np/smartphones/?spm=a2a0e.searchlist.cate_1_1.2.7c00689b9clhEB&vatsal-impex-pvt-ltd&from=wangpu",
    #     "https://www.daraz.com.np/smartphones/infinix/?spm=a2a0e.seller.cate_1_1.4.ad093056ouY36f",
    #     "https://www.daraz.com.np/smartphones/?q=motorola&from=input",
    #     "https://www.daraz.com.np/smartphones/realme/?spm=a2a0e.searchlist.cate_1_1.8.22e6143eZywjWy",
    #     "https://www.daraz.com.np/smartphones/apple/?spm=a2a0e.searchlistcategory.cate_1_1.7.552f3d69Mlqlx5",
    #     "https://www.daraz.com.np/smartphones/nokia/?spm=a2a0e.searchlistcategory.cate_1_1.9.12e2ca9ejohwVM",
    #     "https://www.daraz.com.np/smartphones/vivo/?spm=a2a0e.searchlistcategory.cate_1_1.5.3ff4917bsU3zJf",
    #     "https://www.daraz.com.np/smartphones/oppo/?spm=a2a0e.searchlistcategory.cate_1_1.6.4bf879d9Twv8nH",
    #     "https://www.daraz.com.np/smartphones/alcatel1/",
    #     "https://www.daraz.com.np/smartphones/micromax/",
    #     "https://www.daraz.com.np/tablets/",
    #     "https://www.daraz.com.np/tablets/samsung/",
    #     "https://www.daraz.com.np/tablets/apple/",
    #     "https://www.daraz.com.np/tablets/huawei_brand/",
    #     "https://www.daraz.com.np/tablets/?q=Alcatel+tab&from=input",
    #     "https://www.daraz.com.np/tablets/amazon/",
    #     "https://www.daraz.com.np/laptops/",
    #     "https://www.daraz.com.np/desktop-computer/",
    #     "https://www.daraz.com.np/gaming-consoles/",
    #     "https://www.daraz.com.np/camera/",
    #     "https://www.daraz.com.np/multi-function-printers/",
    #     "https://www.daraz.com.np/mobiles-tablets-accessories/",
    #     "https://www.daraz.com.np/audio/",
    #     "https://www.daraz.com.np/wearable-technology/",
    #     "https://www.daraz.com.np/gaming-accessories/",
    #     "https://www.daraz.com.np/camera-accessories/",
    #     "https://www.daraz.com.np/computing-peripherals-accessories/",
    #     "https://www.daraz.com.np/computing-storage/",
    #     "https://www.daraz.com.np/components-spare-parts/",
    #     "https://www.daraz.com.np/networking/",
    #     "https://www.daraz.com.np/multi-function-printers/",
    #     "https://www.daraz.com.np/televisions/?spm=a2a0e.pdp.breadcrumb.2.479371ccITiyaq",
    #     "https://www.daraz.com.np/tv-accessories/",
    #     "https://www.daraz.com.np/consumer-electronics/",
    #     "https://www.daraz.com.np/cooking-appliances/?page=1&sort=popularity&spm=a2a0e.pdp.breadcrumb.2.437b5bdfT9gbVi",
    #     "https://www.daraz.com.np/small-kitchen-appliances/",
    #     "https://www.daraz.com.np/cooling-heating/",
    #     "https://www.daraz.com.np/floorcare-appliances/",
    #     "https://www.daraz.com.np/garment-care/",
    #     "https://www.daraz.com.np/bath-body/",
    #     "https://www.daraz.com.np/health-beauty-tools/",
    #     "https://www.daraz.com.np/fragrances/",
    #     "https://www.daraz.com.np/hair-care/",
    #     "https://www.daraz.com.np/womens-make-up/",
    #     "https://www.daraz.com.np/mens-grooming/",
    #     "https://www.daraz.com.np/personal-care/",
    #     "https://www.daraz.com.np/skincare/",
    #     "https://www.daraz.com.np/health-supplements/",
    #     "https://www.daraz.com.np/health-care/",
    #     "https://www.daraz.com.np/baby-diapers/",
    #     "https://www.daraz.com.np/baby-gear/",
    #     "https://www.daraz.com.np/baby-personal-care/",
    #     "https://www.daraz.com.np/baby-clothings-accessories/",
    #     "https://www.daraz.com.np/baby-toddler-diapers-potties/",
    #     "https://www.daraz.com.np/feeding/",
    #     "https://www.daraz.com.np/baby-toddler-nursery/",
    #     "https://www.daraz.com.np/baby-toddler-toys-games/",
    #     "https://www.daraz.com.np/toys-games/",
    #     "https://www.daraz.com.np/remote-control-toys-and-play-vehicles/",
    #     "https://www.daraz.com.np/sports-and-outdoor-play/",
    #     "https://www.daraz.com.np/pacifiers-and-accessories/?spm=a2a0e.searchlist.breadcrumb.3.19cb5b37outm3t",
    #     "https://www.daraz.com.np/wow/camp/daraz/megascenario/np/d-mart/home?spm=a2a0e.11779170.feature_nav.1.287d2d2bDkaCgy&hybrid=1&scm=1003.4.icms-zebra-100031662-2974971.OTHER_6029322094_6625879",
    #     "https://www.daraz.com.np/beverages/",
    #     "https://www.daraz.com.np/breakfast/",
    #     "https://www.daraz.com.np/canned-packaged-foods/",
    #     "https://www.daraz.com.np/groceries-baking-cooking-cooking-ingredients/",
    #     "https://www.daraz.com.np/laundry-and-home-care/",
    #     "https://www.daraz.com.np/wines-beers-spirits/",
    #     "https://www.daraz.com.np/pet-supplies-shop/",
    #     "https://www.daraz.com.np/bath/",
    #     "https://www.daraz.com.np/bedding/?spm=a2a0e.searchlistcategory.breadcrumb.3.6b6912c24LfJkb",
    #     "https://www.daraz.com.np/home-decoration/",
    #     "https://www.daraz.com.np/furniture/",
    #     "https://www.daraz.com.np/kitchen-dining/",
    #     "https://www.daraz.com.np/lighting/",
    #     "https://www.daraz.com.np/laundry-cleaning/",
    #     "https://www.daraz.com.np/home-improvement-tools/",
    #     "https://www.daraz.com.np/stationery-craft/",
    #     "https://www.daraz.com.np/books-games-music/",
    #     "https://www.daraz.com.np/musical-instruments/",
    #     "https://www.daraz.com.np/digital-goods/",
    #     "https://www.daraz.com.np/womens-clothing/",
    #     "https://www.daraz.com.np/womens-traditional-clothing/",
    #     "https://www.daraz.com.np/womens-bags/",
    #     "https://www.daraz.com.np/womens-shoes/",
    #     "https://www.daraz.com.np/womens-accessories/",
    #     "https://www.daraz.com.np/womens-lingerie-sleepwear/",
    #     "https://www.daraz.com.np/girls/",
    #     "https://www.daraz.com.np/mens-clothing/",
    #     "https://www.daraz.com.np/mens-bags/",
    #     "https://www.daraz.com.np/mens-shoes/",
    #     "https://www.daraz.com.np/men-accessories/",
    #     "https://www.daraz.com.np/fashion-boys/",
    #     "https://www.daraz.com.np/clothing-men-underwear/",
    #     "https://www.daraz.com.np/mens-watches/",
    #     "https://www.daraz.com.np/womens-watches/",
    #     "https://www.daraz.com.np/kids-watches-wsj/",
    #     "https://www.daraz.com.np/sunglasses/",
    #     "https://www.daraz.com.np/eyeglasses/",
    #     "https://www.daraz.com.np/womens-jewellery/",
    #     "https://www.daraz.com.np/mens-jewellery/",
    #     "https://www.daraz.com.np/mens-sports/",
    #     "https://www.daraz.com.np/womens-sports/",
    #     "https://www.daraz.com.np/outdoor-activities/",
    #     "https://www.daraz.com.np/exercise-fitness/",
    #     "https://www.daraz.com.np/water-sports/",
    #     "https://www.daraz.com.np/racket-sports/",
    #     "https://www.daraz.com.np/team-sports/",
    #     "https://www.daraz.com.np/sports-water-bottles/",
    #     "https://www.daraz.com.np/travels/",
    #     "https://www.daraz.com.np/sp-nutrition/",
    #     "https://www.daraz.com.np/automotive/",
    #     "https://www.daraz.com.np/motorcycle/",
    #     "https://www.daraz.com.np/automotive-exterior-vehicle-care/",
    #     "https://www.daraz.com.np/car-electronics-accessories/",
    #     "https://www.daraz.com.np/motorcycle-parts-spares/",
    #     "https://www.daraz.com.np/motorcycle-riding-gear/",
    #     "https://www.daraz.com.np/motorcycle-helmets/",
    #     "https://www.daraz.com.np/motorcycle-gloves/",
    #     "https://www.daraz.com.np/interior-accessories/",
    #     "https://www.daraz.com.np/engine-oils-fluids/",
    #     "https://www.daraz.com.np/wheels-tires/",
    #     "https://www.daraz.com.np/car-care-lubricants/?spm=a2a0e.searchlistcategory.card.1.241b5c25sIXItt&item_id=103346231&from=onesearch_category_3257"
    # ]
    start_urls = [
        # "https://hamrobazaar.com/c6-apparels-and-accessories",
        # "https://hamrobazaar.com/c92-apparels-and-accessories-sunglasses",
        # "https://hamrobazaar.com/c149-apparels-and-accessories-watches",
        # "https://hamrobazaar.com/c93-apparels-and-accessories-women-s-clothing",
        # "https://hamrobazaar.com/c90-apparels-and-accessories-men-s-clothing",
        # "https://hamrobazaar.com/c6-apparels-and-accessories",
        # "https://hamrobazaar.com/c1-automobiles",
        # "https://hamrobazaar.com/c62-automobiles-motorcycle",
        # "https://hamrobazaar.com/c48-automobiles-cars",
        # "https://hamrobazaar.com/c13-automobiles-parts-and-accessories",
        # "https://hamrobazaar.com/c235-automobiles-showroom-cars",
        # "https://hamrobazaar.com/c132-automobiles-showroom-motorcycle",
        # "https://hamrobazaar.com/c1-automobiles",
        # "https://hamrobazaar.com/c9-beauty-and-health",
        # "https://hamrobazaar.com/c146-beauty-and-health-medical-and-health-devices",
        # "https://hamrobazaar.com/c85-beauty-and-health-electronic-cigarette-and-vape",
        # "https://hamrobazaar.com/c155-beauty-and-health-others",
        # "https://hamrobazaar.com/c9-beauty-and-health",
        # "https://hamrobazaar.com/c10-books-and-learning",
        # "https://hamrobazaar.com/c260-business-and-industrial",
        # "https://hamrobazaar.com/c229-business-and-industrial-security-and-cctv",
        # "https://hamrobazaar.com/c199-business-and-industrial-office-furniture-and-fixtures",
        "https://hamrobazaar.com/c263-business-and-industrial-tool-and-small-machines",
        # "https://hamrobazaar.com/c260-business-and-industrial",
        # "https://hamrobazaar.com/c3-computer-and-peripherals",
        # "https://hamrobazaar.com/c22-computer-and-peripherals-laptops",
        # "https://hamrobazaar.com/c21-computer-and-peripherals-tablet-pc-and-ipads",
        # "https://hamrobazaar.com/c20-computer-and-peripherals-desktop-pc",
        # "https://hamrobazaar.com/c188-computer-and-peripherals-networking-equipments",
        # "https://hamrobazaar.com/c3-computer-and-peripherals",
        # "https://hamrobazaar.com/c4-electronics",
        # "https://hamrobazaar.com/c96-electronics-digital-camera",
        # "https://hamrobazaar.com/c100-electronics-projectors",
        # "https://hamrobazaar.com/c101-electronics-television",
        # "https://hamrobazaar.com/c274-electronics-portable-bluetooth-speakers",
        # "https://hamrobazaar.com/c4-electronics",
        # "https://hamrobazaar.com/c130-events-and-happenings",
        # "https://hamrobazaar.com/c7-home-furnishing-and-appliances",
        # "https://hamrobazaar.com/c121-home-furnishing-and-appliances-kitchen-appliances",
        # "https://hamrobazaar.com/c120-home-furnishing-and-appliances-home-furniture",
        # "https://hamrobazaar.com/c122-home-furnishing-and-appliances-home-appliances",
        # "https://hamrobazaar.com/c7-home-furnishing-and-appliances",
        # "https://hamrobazaar.com/c221-jobs",
        # "https://hamrobazaar.com/c2-mobile-and-accessories",
        # "https://hamrobazaar.com/c41-mobile-and-accessories-accessories",
        # "https://hamrobazaar.com/c31-mobile-and-accessories-handsets",
        # "https://hamrobazaar.com/c2-mobile-and-accessories",
        # "https://hamrobazaar.com/c8-music-instrument",
        # "https://hamrobazaar.com/c241-pets-and-pet-care",
        # "https://hamrobazaar.com/c112-real-estate",
        # "https://hamrobazaar.com/c191-real-estate-business-and-shop-for-sale",
        # "https://hamrobazaar.com/c202-real-estate-for-rent-flat-and-apartment",
        # "https://hamrobazaar.com/c114-real-estate-for-rent-house",
        # "https://hamrobazaar.com/c205-real-estate-for-rent-office-space",
        # "https://hamrobazaar.com/c113-real-estate-for-sale-house",
        # "https://hamrobazaar.com/c201-real-estate-for-sale-land",
        # "https://hamrobazaar.com/c317-real-estate-new-housing-apartment-project",
        # "https://hamrobazaar.com/c112-real-estate",
        # "https://hamrobazaar.com/c135-services",
        # "https://hamrobazaar.com/c158-services-other-services",
        # "https://hamrobazaar.com/c254-services-home-construct-and-design",
        # "https://hamrobazaar.com/c255-services-advertisingprintingpublication",
        # "https://hamrobazaar.com/c135-services",
        # "https://hamrobazaar.com/c299-sports-and-fitness",
        # "https://hamrobazaar.com/c5-toys-and-video-games",
        # "https://hamrobazaar.com/c139-travel-tour-and-packages",
        # "https://hamrobazaar.com/c167-want-to-buy-buyer-list",
        # "https://hamrobazaar.com/c179-want-to-buy-buyer-list-real-estate",
        # "https://hamrobazaar.com/c177-want-to-buy-buyer-list-mobile-and-accessories",
        # "https://hamrobazaar.com/c173-want-to-buy-buyer-list-car-and-bikes",
        # "https://hamrobazaar.com/c171-want-to-buy-buyer-list-services",
        # "https://hamrobazaar.com/c167-want-to-buy-buyer-list"
    ]

    def parse(self, response):
        # links1= response.xpath("//div[@class='sku -gallery -validate-size ']/a[@class='link']/@href").extract()
        # links2= response.xpath("//div[@class='sku -gallery ']/a[@class='link']/@href").extract()
        self.logger.info('A response from %s just arrived!', response.url)
        links = response.xpath("//a[@target='_blank']/@href").extract()
        # links= links1 + links2

        # self.logger.info(links)
        for link in links:
            print(link)
            if '.html' in link:
                time.sleep(3)
                yield Request('https://hamrobazaar.com/'+link, callback=self.parse_article, dont_filter=True)
        #
        # nextpageurl = response.xpath('//li/a[@title="Next"]/@href').extract_first()
        # absolute_next_page_url = response.urljoin(nextpageurl)
        # yield scrapy.Request(nextpageurl, dont_filter=True)


    def parse_article(self,response):

        title =  response.xpath('//span[@class="title"]/b/font/text()').extract_first()
        seller = response.xpath('//td[@id="white"]/text()').extract()[11]
        price = response.xpath('//font[@class="bigprice"]/text()').extract()[0]
        item = response.xpath('//a/u/text()').extract()
        each = item.pop()
        while each!= 'For more read Safety Tips':
            each = item.pop()
        category= item.pop()
        image = response.xpath('//img[@id="inimg"]/@src').extract_first()

        yield{

            'Title':title,
            "Category":category,
            'Price':price,
            'Seller_name':"".join(seller.split()),
            "image": image


            }
