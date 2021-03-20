import scrapy


class NecklaceSetsSpider(scrapy.Spider):
    """ scrapy.Spider class to scrape the necklace sets on houseofindia.com"""

    name = "necklace_sets"

    # Starting on the necklace-sets category on the jewelry section
    start_urls = [
        'https://www.houseofindya.com/zyra/necklace-sets/cat',
    ]

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

