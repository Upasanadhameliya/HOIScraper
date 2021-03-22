import scrapy


class JewelrySpider(scrapy.Spider):
    """ scrapy.Spider class to scrape the necklace sets on houseofindia.com"""

    name = "jewelry"

    def start_requests(self):
        # Starting on the necklace-sets category on the jewelry section
        url = 'https://www.houseofindya.com/zyra/necklace-sets/cat'
        category = getattr(self, 'cat', None)
        
        if getattr(self,'all','False').upper() == "TRUE":
            setattr(self,'all',True)
            all_categories = True
        else:
            setattr(self,'all',False)
            all_categories = False

        url = 'https://www.houseofindya.com/zyra/' \
            if all_categories else \
            'https://www.houseofindya.com/zyra/'+category+'/cat' \
            if category is not None else \
            'https://www.houseofindya.com/zyra/necklace-sets/cat'


        if all_categories:
            yield scrapy.Request(url, callback = self.parse)
        else:
            yield scrapy.Request(url, callback = self.parse_cat)


    def parse(self,response):
        # print("Url is:")
        # print(response.request.url)

        # categories_urls = response.css("div.seecatgTitle a::attr(href)").getall()
        categories_urls = response.xpath('//div[@class="seecatgTitle"]/a/@href').getall()
        # categories_urls = response.css("div.seecatgTitle").xpath('/a').getall()
        categories_urls = list(map(lambda x:'https://www.houseofindya.com'+x,categories_urls))
        print(categories_urls)

        for index,cat_url in enumerate(categories_urls,1):
            print("parse for loop url: "+cat_url)
            # if index == 3:
            #     break
            yield scrapy.Request(cat_url, callback = self.parse_cat)


    # Parsing the response object
    def parse_cat(self, response):
        print("Called for is:")
        print(response.request.url)

        category = str(response.request.url).split('/')[-2]

        # Looping through <li> under <ul id="JsonProductList">
        for li_obj in response.xpath('//ul[@id="JsonProductList"]/li'):
            # response_dict = {
            #     'set_id': li_obj.css("::attr(data-pos)").get(),
            #     'description': li_obj.css("::attr(data-name)").get(),
            #     'price': li_obj.css("::attr(data-price)").get(),
            #     'img_url_1': li_obj.css("a div.catgItem img::attr(data-original)").get(),
            #     'img_url_2': li_obj.css("a div.catgItem img::attr(onmouseover)").get().strip("this.src=").strip("'"),
            #     'color': li_obj.css("::attr(data-color)").get(),
            # }

            print("Inside for loop parse_cat")
            response_dict = {
                'set_id': li_obj.css("::attr(data-pos)").get(),
                'description': li_obj.css("::attr(data-name)").get(),
            }

            if getattr(self,'all',False):
                response_dict['category'] = str(response.request.url).split('/')[-2]
            yield response_dict

