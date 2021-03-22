import scrapy


class JewelrySpider(scrapy.Spider):
    """ scrapy.Spider class to scrape the necklace sets on houseofindia.com"""

    name = "jewelry"

    def start_requests(self):
        # Get the command line argument 'cat' into category variable
        category = getattr(self, 'cat', None)
        
        # Get the 'all' command line argument and check if it's true
        if getattr(self,'all','False').upper() == "TRUE":
            # if true then set it to a boolean True variable instead of string
            setattr(self,'all',True)
            all_categories = True
        else:
            # if false then set it to a boolean False variable instead of string
            setattr(self,'all',False)
            all_categories = False

        # Set the url based on the command line arguments passed
        url = 'https://www.houseofindya.com/zyra/' \
            if all_categories else \
            'https://www.houseofindya.com/zyra/'+category+'/cat' \
            if category is not None else \
            'https://www.houseofindya.com/zyra/necklace-sets/cat'


        # Call self.parse in case of all categories
        if all_categories:
            yield scrapy.Request(url, callback = self.parse)
        # Call self.parse_cat for just one category
        else:
            yield scrapy.Request(url, callback = self.parse_cat)

    # Parsing the top level response object
    def parse(self,response):

        # Get the categories_urls from the /zyra/ page for all categories and make 
        # proper houseofindya urls
        categories_urls = response.xpath('//div[@class="seecatgTitle"]/a/@href').getall()
        categories_urls = list(map(lambda x:'https://www.houseofindya.com'+x,categories_urls))

        # For each category in the urls call the self.parse_cat function
        for cat_url in categories_urls:
            yield scrapy.Request(cat_url, callback = self.parse_cat)


    # Parsing the category response object
    def parse_cat(self, response):
        
        # Looping through <li> under <ul id="JsonProductList">
        for li_obj in response.xpath('//ul[@id="JsonProductList"]/li'):
            response_dict = {
                'set_id': li_obj.css("::attr(data-pos)").get(),
                'description': li_obj.css("::attr(data-name)").get(),
                'price': li_obj.css("::attr(data-price)").get(),
                'img_url_1': li_obj.css("a div.catgItem img::attr(data-original)").get(),
                'img_url_2': li_obj.css("a div.catgItem img::attr(onmouseover)").get().strip("this.src=").strip("'"),
                'color': li_obj.css("::attr(data-color)").get(),
            }

            # Add a field of category for 'all' attribute set to True
            if getattr(self,'all',False):
                response_dict['category'] = str(response.request.url).split('/')[-2]
            yield response_dict

