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

### Jewelry spider for a particular category under jewelry section
From the webscraper directory run the following command:
1. csv :
```
scrapy crawl jewelry -O <filename>.csv -a cat=hair-jewelry
```
2. json:
```
scrapy crawl jewelry -O <filename>.json -a cat=hair-jewelry
```

### Jewelry spider for all categories under jewelry section
From the webscraper directory run the following command:
1. csv :
```
scrapy crawl jewelry -O <filename>.csv -a all=true
```
2. json:
```
scrapy crawl jewelry -O <filename>.json -a all=true
```
Scrapes and saves all items with their category names in a separate field


# Output

###### Necklace Sets CSV File 
![Alt text](Screenshots/Screenshot1.png?raw=true "Necklace sets csv")

All other output files are under "Output" folder
