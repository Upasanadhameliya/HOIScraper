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

        print("Response css: div")
        print(response.css("div"))

        # page = response.url.split("/")[-2]
        # print("Page is:")
        # print(page)

        # filename = f'quotes-{page}.html'
        
        # print("Filename is:")
        # print(filename)
        # with open(filename, 'wb') as f:
        #     print("writing to file")
        #     f.write(response.body)
        # self.log(f'Saved file {filename}')