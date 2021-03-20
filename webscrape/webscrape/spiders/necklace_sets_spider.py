import scrapy


class QuotesSpider(scrapy.Spider):
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
        [print(i) for i in necklace_div.css("ul li::attr(data-name)").getall()]
