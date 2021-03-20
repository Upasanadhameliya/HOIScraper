import scrapy


class NecklaceSetsSpider(scrapy.Spider):
    name = "necklace_sets"

    start_urls = [
        'https://www.houseofindya.com/zyra/necklace-sets/cat',
    ]

    def parse(self, response):
        print("Response is :")
        print(response)
        print("Response url:")
        print(response.url)

        print("Response css: div.catgList")
        print(response.css("div.catgList")[0])

        necklace_div = response.css("div.catgList")[0]

        print("A different approach:")
        # [print(i) for i in necklace_div.css("ul li::attr(data-name)").getall()]
        for li_obj in necklace_div.css("ul li"):
            yield {
                'set_id': li_obj.css("::attr(data-pos)").get(),
                'description': li_obj.css("::attr(data-name)").get(),
                'price': li_obj.css("::attr(data-price)").get(),
                'img_url_1': li_obj.css("a div.catgItem img::attr(data-original)").get(),
                'img_url_2': li_obj.css("a div.catgItem img::attr(onmouseover)").get().strip("this.src=").strip("'")
            }

