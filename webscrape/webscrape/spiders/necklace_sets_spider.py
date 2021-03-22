import scrapy


class JewelrySpider(scrapy.Spider):
    """ scrapy.Spider class to scrape the necklace sets on houseofindia.com"""

    name = "jewelry"

    
    # start_urls = [
    #     'https://www.houseofindya.com/zyra/necklace-sets/cat',
    # ]

    def start_requests(self):
        # Starting on the necklace-sets category on the jewelry section
        url = 'https://www.houseofindya.com/zyra/necklace-sets/cat'
        category = getattr(self, 'cat', None)
        if category is not None:
            url = 'https://www.houseofindya.com/zyra/'+category+'/cat'
        yield scrapy.Request(url, self.parse)

    # Parsing the response object
    def parse(self, response):

        # Looping through <li> under <ul id="JsonProductList">
        for li_obj in response.xpath('//ul[@id="JsonProductList"]/li'):
            yield {
                'set_id': li_obj.css("::attr(data-pos)").get(),
                'description': li_obj.css("::attr(data-name)").get(),
                'price': li_obj.css("::attr(data-price)").get(),
                'img_url_1': li_obj.css("a div.catgItem img::attr(data-original)").get(),
                'img_url_2': li_obj.css("a div.catgItem img::attr(onmouseover)").get().strip("this.src=").strip("'"),
                'color': li_obj.css("::attr(data-color)").get()
            }

