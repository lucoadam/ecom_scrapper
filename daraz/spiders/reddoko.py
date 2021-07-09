# -*- coding: utf-8 -*-
import scrapy
from scrapy import Request
from scrapy.spiders import Rule
import time


class RedDokoSpider(scrapy.Spider):
    name = 'reddoko'
    allowed_domains = ['daraz.com.np']


    start_urls = [
        "https://www.reddoko.com/categories/western-wear",
        "https://www.reddoko.com/categories/dress",
        "https://www.reddoko.com/categories/jeans",
        "https://www.reddoko.com/categories/western-wear-jackets",
        "https://www.reddoko.com/categories/tops",
        "https://www.reddoko.com/categories/trousers",
        "https://www.reddoko.com/categories/shorts",
        "https://www.reddoko.com/categories/outer",
        "https://www.reddoko.com/categories/skirt",
        "https://www.reddoko.com/categories/legging",
        "https://www.reddoko.com/categories/lehenga",
        "https://www.reddoko.com/categories/kurtis",
        "https://www.reddoko.com/categories/saree",
        "https://www.reddoko.com/categories/personal-care",
        "https://www.reddoko.com/categories/daily-needs-makeup-lipstick",
        "https://www.reddoko.com/categories/daily-needs-makeup-compact-powder",
        "https://www.reddoko.com/categories/daily-needs-makeup-manicure-kit",
        "https://www.reddoko.com/categories/daily-needs-makeup-nail-polish",
        "https://www.reddoko.com/categories/personal-care",
        "https://www.reddoko.com/categories/watches",
        "https://www.reddoko.com/categories/women-watches",
        "https://www.reddoko.com/categories/footwear-womens-footwear",
        "https://www.reddoko.com/categories/footwear-womens-footwear-flat-slipon-sandal",
        "https://www.reddoko.com/categories/womens-fashion-lingerie-sleepwear",
        "https://www.reddoko.com/categories/womens-fashion-lingerie-sleepwear-tanks-spagettis",
        "https://www.reddoko.com/categories/womens-fashion-lingerie-sleepwear-innerwear",
        "https://www.reddoko.com/categories/mens-fashion",
        "https://www.reddoko.com/categories/men-tshirt",
        "https://www.reddoko.com/categories/mens-shirt",
        "https://www.reddoko.com/categories/men-jeans",
        "https://www.reddoko.com/categories/mens-fashion-suits-blazers",
        "https://www.reddoko.com/categories/men-shorts",
        "https://www.reddoko.com/categories/men-trouser",
        "https://www.reddoko.com/categories/footwear-mens-footwear",
        "https://www.reddoko.com/categories/footwear-mens-footwear-casual-shoes",
        "https://www.reddoko.com/categories/footwear-mens-footwear-formal-shoes",
        "https://www.reddoko.com/categories/footwear-mens-footwear-sports-shoes",
        "https://www.reddoko.com/categories/footwear-mens-footwear-working-shoes",
        "https://www.reddoko.com/categories/footwear-mens-footwear-outdoor-shoes",
        "https://www.reddoko.com/categories/footwear-mens-footwear-sandal-floaters",
        "https://www.reddoko.com/categories/footwear-mens-footwear-loafers-moccasins",
        "https://www.reddoko.com/categories/men-watches",
        "https://www.reddoko.com/categories/bags-luggage-backpacks-more",
        "https://www.reddoko.com/categories/fashion-accessories-mens-wallet",
        "https://www.reddoko.com/categories/mens-fashion-innerwear-sleepwear",
        "https://www.reddoko.com/categories/mens-fashion-innerwear-sleepwear-underwear",
        "https://www.reddoko.com/categories/mens-fashion-innerwear-sleepwear-vest",
        "https://www.reddoko.com/categories/toys-games",
        "https://www.reddoko.com/categories/toys-games-educational-toys",
        "https://www.reddoko.com/categories/toys-games-puzzle-cubes",
        "https://www.reddoko.com/categories/toys-games-activity-sets",
        "https://www.reddoko.com/categories/toys-games-dolls-doll-homes",
        "https://www.reddoko.com/categories/children-book",
        "https://www.reddoko.com/categories/daily-needs-baby-care",
        "https://www.reddoko.com/categories/daily-needs-baby-care-health-safety",
        "https://www.reddoko.com/categories/daily-needs-baby-care-nursing-feeding",
        "https://www.reddoko.com/categories/daily-needs-baby-care-bathing-skin-care",
        "https://www.reddoko.com/categories/daily-needs-baby-care-baby-grooming",
        "https://www.reddoko.com/categories/daily-needs-baby-care-potty-training-and-diapers",
        "https://www.reddoko.com/categories/prams-baby-gear",
        "https://www.reddoko.com/categories/literature-fiction",
        "https://www.reddoko.com/categories/children-book",
        "https://www.reddoko.com/categories/spirituality",
        "https://www.reddoko.com/categories/politics",
        "https://www.reddoko.com/categories/travel",
        "https://www.reddoko.com/categories/battery-grips",
        "https://www.reddoko.com/categories/lens",
        "https://www.reddoko.com/categories/camera-flash",
        "https://www.reddoko.com/categories/mobile-phone",
        "https://www.reddoko.com/categories/tablet",
        "https://www.reddoko.com/categories/robotics-electronics",
        "https://www.reddoko.com/categories/sensor-modules",
        "https://www.reddoko.com/categories/arduino-shield",
        "https://www.reddoko.com/categories/cables-connectors",
        "https://www.reddoko.com/categories/microcontroller-other-ics",
        "https://www.reddoko.com/categories/mobile-tablet-accessories",
        "https://www.reddoko.com/categories/mobile-tablet-accessories-wearable-smart-watches",
        "https://www.reddoko.com/categories/mobile-tablet-accessories-selfie-stick-and-stand",
        "https://www.reddoko.com/categories/tvs-audio-videos",
        "https://www.reddoko.com/categories/tvs-audio-videos-televisions",
        "https://www.reddoko.com/categories/tvs-audio-videos-audio-system",
        "https://www.reddoko.com/categories/tvs-audio-videos-projectors-and-accessories",
        "https://www.reddoko.com/categories/tvs-audio-videos-speakers",
        "https://www.reddoko.com/categories/protein-suppliments",
        "https://www.reddoko.com/categories/sports-fitness-fitness-accessories",
        "https://www.reddoko.com/categories/pet-supplies",
        "https://www.reddoko.com/categories/pet-supplies-dog-biscuits-treats",
        "https://www.reddoko.com/categories/pet-supplies-pets-accessories-petgrooming",
        "https://www.reddoko.com/categories/pet-supplies-pet-food",
        "https://www.reddoko.com/categories/pet-supplies-supplements",
        "https://www.reddoko.com/categories/appliances",
        "https://www.reddoko.com/categories/appliances-large-appliances-refrigerators",
        "https://www.reddoko.com/categories/appliances-large-appliances-washing-machine",
        "https://www.reddoko.com/categories/appliances-large-appliances-microwaves",
        "https://www.reddoko.com/categories/furniture",
        "https://www.reddoko.com/categories/furniture-bean-bags",
        "https://www.reddoko.com/categories/appliances-kitchen-appliances",
        "https://www.reddoko.com/categories/appliances-kitchen-appliances-rice-cooker-others",
        "https://www.reddoko.com/categories/appliances-kitchen-appliances-juicer-mixer-grinder",
        "https://www.reddoko.com/categories/appliances-kitchen-appliances-gas-stoves",
        "https://www.reddoko.com/categories/appliances-kitchen-appliances-water-dispensers-accessories",
        "https://www.reddoko.com/categories/appliances-kitchen-appliances-toasters-and-sandwich-maker"
    ]


    def parse(self, response):
        # links1= response.xpath("//div[@class='sku -gallery -validate-size ']/a[@class='link']/@href").extract()
        # links2= response.xpath("//div[@class='sku -gallery ']/a[@class='link']/@href").extract()
        self.logger.info('A response from %s just arrived!', response.url)
        links = response.xpath("//a/@data-product-layer").extract()
        for link in links:
            import json
            link = json.loads(link)
            print(link['name'])
            yield {
                "Type": "simple",
                "SKU": link['sku'],
                'Name': link['name'],
                "Published":1,
                "Is featured?":1,
                "Visibility in catalog": "visible",
                "Short description": "This is product description",
                "Description":link['description'] if 'description' in link and link['description']!=None else 'This is description',
                "Date sale price starts":"",
                "Date sale price ends":"",
                "Tax status":"taxable",
                "Tax class":"",
                "In stock?":1,
                "Stock": 100,
                "Allow customer reviews?":1,
                "Categories": "> ".join([cat['name'] for cat in link['categories']]),
                'Regular price': int(link['price'])*1.12,
                'Sale price': int(link['price']),
                "Images": ",".join(['https://www.reddoko.com/uploads/'+str(image['media_id'])+'/'+image['file'] for image in link['images']])
            }
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
        title = response.xpath("//div/h2[@class='lg-title']/text()").extract_first()
        price = response.xpath("//h3/text()").extract_first()
        category = response.xpath("//div/span[@class='xs-title']/text()").extract_first()
        seller = ""

        images = response.xpath("//ul[@class='exzoom_img_ul']/li/img/@src").extract()

        yield {
            "ID":"",
            "Type": "simple",
            "SKU": "-".join("".join("".join("".join("".join(title.split("/")).split(",")).split(")")).split("(")).lower().split()),
            'Name': title,
            "Published":1,
            "Is featured?":1,
            "Visibility in catalog": "visible",
            "Short description": "This is product description",
            "Description":"<p>Iste curae sed a accusantium rerum dui ac itaque, veritatis, repudiandae deleniti perspiciatis placerat, odio fuga orci odio molestie, montes, laoreet culpa habitant labore eu mollitia sodales! Aspernatur dictumst massa velit sollicitudin quam vel placerat, anim, magnam blandit blanditiis dignissim pariatur porro sapien nascetur ullamcorper quod augue luctus mollis magnis, harum fames vero neque, sed? Lectus, voluptatum voluptates laudantium potenti. Ad vitae, sit animi per eaque, delectus saepe, cursus vero expedita aliquam expedita taciti, occaecati voluptatum dui, cupidatat tempore recusandae voluptate aute wisi dis ad, luctus, maecenas? Dignissimos integer pulvinar, suspendisse class cras reprehenderit curabitur? Quisque! Tempora occaecati est leo.</p> <p>Quis fuga eiusmod aperiam voluptate curae vero illo ratione libero, quia praesent euismod voluptate consequat debitis magna! Consectetuer iste! Nullam quas. Nostrud? Minus hendrerit. Tortor lacinia mauris, sollicitudin nonummy quasi, error, aliquip laoreet, recusandae nam potenti? Dui, scelerisque cum cubilia, conubia, enim? Penatibus magna pretium! Orci. Sem molestie pariatur sed eveniet fames turpis interdum! Velit, esse dolore potenti eaque tempor primis maecenas donec parturient unde temporibus viverra beatae cubilia ipsam vulputate per quod maecenas quo cillum! Dignissimos habitasse massa ultrices, tempus, expedita ornare fringilla! Senectus blandit quod voluptatibus fusce assumenda. Condimentum nec ratione, omnis id ridiculus harum fugit, do, integer.</p> <p>Curae praesentium phasellus deserunt donec platea, sequi eiusmod perferendis adipiscing sociosqu erat cum cupiditate mollis soluta irure delectus, elementum occaecati cras sunt etiam integer! Iure deserunt totam blandit, iure adipisicing, assumenda ipsum repellendus? Occaecati! Proident inceptos purus pulvinar pede atque lorem nisl, erat quasi id id, fugiat feugiat? Scelerisque eleifend, commodi, iure ipsum rutrum. Aliquam, facilisis, illo facere aperiam habitant, vitae lobortis eros omnis luctus! Tincidunt eiusmod rerum penatibus molestiae, iste repellendus mollitia dignissimos urna excepturi? Proin turpis, vehicula tenetur fringilla, donec fringilla vitae! Nunc velit commodo magna nostra leo? Dolore rutrum quae laoreet suscipit sociosqu, magnam? Conubia, adipiscing class.</p> <p>Adipisicing platea lorem scelerisque. Dictum nonummy consequatur ipsa varius unde quisquam adipiscing! Earum nobis, explicabo. Qui volutpat, dapibus morbi hymenaeos, modi, maiores praesentium quibusdam. Nunc accusantium. Vero molestiae aptent massa. Hac veniam. Montes ea pariatur voluptatem, veniam, laborum lorem aliquam temporibus adipisci, voluptatibus excepturi quasi elit cursus corporis! Perferendis malesuada adipisci fugit hic vestibulum! Exercitationem. Voluptatum. Repellat, minim ipsum mus, repudiandae praesent distinctio condimentum deserunt, maxime sociis? Irure sociis, molestias, dui fringilla, placeat distinctio nobis parturient taciti fugit? Laborum ipsam? Cursus ad repudiandae, suspendisse, primis, excepturi nostrud, voluptates quasi penatibus impedit sed voluptates per rutrum quaerat dolor! Accumsan repellat sagittis.</p> <p>Ipsam, hac platea occaecati. Aliquip ipsa, molestiae. Quisquam integer, modi sapiente pede, convallis nemo eligendi, inventore, quia feugiat, eaque fusce adipiscing phasellus quidem voluptatem accusantium metus sit turpis volutpat nemo? Doloremque sagittis commodi eaque magni nihil, occaecati malesuada aptent impedit, inventore facilisi autem quaerat volutpat, aliquip ipsam dis, facere ea, fusce error dolor urna! Reiciendis cubilia, nisi maxime! Dictumst. Quisquam? Elit, consequat sit recusandae proident eveniet ut saepe, aptent porro molestias class tellus cumque! Ipsum. Tortor orci lorem torquent exercitation sociosqu convallis natoque feugiat varius sint quam laboriosam tempor sed, tellus natoque quas magnam earum primis? Nascetur aptent! Animi tincidunt.</p> <p>Laborum aliquid, auctor maxime ea eligendi. Ullamco, ridiculus quisque, commodo vel! Ridiculus quisque reiciendis? Harum consequat feugiat, accusantium aliquip dignissim fugit auctor etiam senectus arcu, sunt, reiciendis explicabo laborum. Irure voluptatum beatae malesuada eveniet elementum harum, commodo vivamus sodales proin, unde praesent id mollis hymenaeos quae quisquam tortor magnam, cursus, ex, similique aute dolorem ex omnis culpa pariatur iusto tempore ipsam consequuntur tortor, justo pulvinar ac similique, rerum occaecat iusto mattis primis, reprehenderit porta erat voluptate nisi adipisci, nisi sequi mattis exercitationem, accumsan deserunt, ratione? Molestias? Consectetuer pharetra commodo temporibus! Natus, magnam, orci dicta dolorem esse debitis dignissim! Incididunt, iste.</p> <p>Inceptos dapibus egestas mattis class optio class sit aenean laoreet orci pariatur culpa imperdiet natoque enim asperiores, aspernatur aspernatur cumque! Tempora mollitia justo quos possimus quidem eveniet lacinia etiam diamlorem? Eu facilisis! Fugit molestiae natoque? Tempora, modi exercitation impedit eaque urna mollis fugiat cursus nam rhoncus nec lectus! Proident commodi, autem sed consectetur habitant, auctor quia viverra nisi cum dolore quod ducimus nisl pharetra sint orci nesciunt tortor montes, hendrerit per laoreet. Libero vero adipisicing aliquid perferendis laoreet, doloribus donec? Cupiditate. Luctus posuere vulputate. Incidunt, tempor veniam imperdiet, eum assumenda eleifend! Similique odit excepturi egestas est fermentum repudiandae, autem, suscipit.</p> <p>Aperiam ipsa aliquid nam irure, nesciunt illo ac. Accumsan exercitation elit magnis facere eligendi? Unde laboriosam. Debitis facilisi, massa adipisicing libero duis dolorem adipiscing. Senectus libero? Feugiat! Nostrum, cillum facilisis cras eleifend, voluptates labore sunt varius, ac minima justo semper, cursus nisl proident pulvinar, modi fames impedit dolores ea erat feugiat tortor mattis officiis mollitia error? Tenetur reprehenderit eget iure, integer nulla nascetur saepe, mattis hendrerit voluptates turpis, nisl eget. Hac maecenas. Feugiat incidunt mus molestiae, torquent, eos bibendum anim habitasse cillum. Enim orci integer volutpat congue exercitation, platea quibusdam. Eum cillum congue luctus fuga. Ab, quaerat minus conubia adipisci.</p> <p>Habitant nisi, turpis quibusdam laborum neque deserunt ullam, magnam qui leo modi, molestiae porta, platea? Congue sociosqu lectus. Aliqua conubia totam reprehenderit pariatur ante facere integer morbi! Scelerisque, mauris. Quibusdam nostrum mollis labore, magnam qui ab, culpa sapiente erat dignissimos voluptates minim class porro, sapiente nulla! Condimentum asperiores, animi cras dolor porttitor, mi voluptates soluta magnam cursus. Pariatur quisque distinctio facilisi totam porta sequi platea netus vivamus class, aperiam, rerum! Dignissim dictum. Mollitia ipsa quaerat laboris vulputate, nulla quaerat earum? Interdum quam ipsa lobortis porro sociosqu? Possimus. Nihil? Laudantium quo! Quis incididunt aliquam aute assumenda, doloribus. Occaecat blandit consequatur est.</p> <p>Ea justo possimus eius voluptates modi eros. Mus laboriosam, excepteur, iaculis tellus excepturi hic repudiandae ullamco aperiam? Nesciunt venenatis! Scelerisque aliquid, aptent laborum? Nesciunt! Quibusdam pede enim natus, ratione hymenaeos? Ultrices purus quisque ullamcorper wisi eaque, doloribus reprehenderit dolores eligendi voluptas adipisicing vestibulum, facilis sociis? Excepteur luctus dictumst? Mi, a rhoncus morbi montes nostra, laoreet veniam arcu illo eum doloribus, excepteur earum habitant? Sit necessitatibus ultricies, praesent lobortis, tempora unde voluptates numquam hic fugit rhoncus hymenaeos facilisis tristique, unde maxime porro? Animi, necessitatibus tempora natoque hac nec. Adipisicing hac, urna, eleifend arcu quaerat wisi rerum quod dis eum eu cumque.</p>",
            "Date sale price starts":"",
            "Date sale price ends":"",
            "Tax status":"taxable",
            "Tax class":"",
            "In stock?":1,
            "Stock": 100,
            "Allow customer reviews?":1,
            "Categories": "Snacks Branded > Breakfast",
            'Regular price': int("".join(("".join(price.split("Rs"))).split()))*1.12,
            'Sale price': int("".join(("".join(price.split("Rs"))).split())),
            "Images": ",".join(images)

        }
