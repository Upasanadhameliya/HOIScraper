# Task - Create scraper for https://www.houseofindya.com


## This repository contains one scrapy spider that can do the following tasks: 
  1. Scrape https://www.houseofindya.com/zyra/necklace-sets/cat : for the category Necklace Sets and create .json and .csv files
  2. Scrape https://www.houseofindya.com/zyra/ for a particular category provided as a command line argument. Eg: cat=hair-jewelry
  3. Scrape https://www.houseofindya.com/zyra/ for all categories when provided with all=true as command line argument

# Install
```
pip install -r requirements.txt
```

# Running the crawlers/spiders

### Jewelry spider for Necklace Sets category
From the webscraper directory run the following command:
1. csv :
```
scrapy crawl jewelry -O <filename>.csv
```
2. json:
```
scrapy crawl jewelry -O <filename>.json
```

### Jewelry spider for a particular category
From the webscraper directory run the following command:
1. csv :
```
scrapy crawl jewelry -O <filename>.csv -a cat=hair-jewelry
```
2. json:
```
scrapy crawl jewelry -O <filename>.json -a cat=hair-jewelry
```

### Jewelry spider for a particular category
From the webscraper directory run the following command:
1. csv :
```
scrapy crawl jewelry -O <filename>.csv -a all=true
```
2. json:
```
scrapy crawl jewelry -O <filename>.json -a all=true
```
Scrapes and saves all quotes with their author and tags.


```
scrapy crawl quotes_scroll -o <filename>.json
```
Scrapes and saves all quotes with their author and tags when the page uses continuous scrolling and not a Nex Page  button.


```
scrapy crawl login_spider -o <filename>.json
```
This spider first performs a login to then access a link to goodreads.com accessible only after the login. Then saves 
The atuhor and their respective page in goodreads.com

# Output

###### FundRazr spider 
![Alt text](screens/fundrazr_screen.png?raw=true "FundRazr csv")

###### SportsDirect spider 
![Alt text](screens/sportsdirect_screen.png?raw=true "SportsDirect JSON")
![Alt text](screens/sportsdirect_screen2.png?raw=true "SportsDirect Downloads")

###### authors spider 
![Alt text](screens/authors.png?raw=true "authors json")

###### quotes/quotes_scroll spider
![Alt text](screens/quotes.png?raw=true "quotes json")

###### login_spider spider
![Alt text](screens/author_goodreadurl.png?raw=true "logn_author_goodreads_url json")
