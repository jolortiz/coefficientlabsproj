import requests
from bs4 import BeautifulSoup
import csv

# list of all pages with products
urls = ['https://theziran.com/collections/accessories', 'https://theziran.com/collections/mens', 'https://theziran.com/collections/intimates', 'https://theziran.com/collections/mens-1', 'https://theziran.com/collections/ugo-mozie-x-ziran', 'https://theziran.com/collections/womens']

# open and write categories for csv file
with open('output.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile, delimiter=',',
                            quotechar='|', quoting=csv.QUOTE_MINIMAL)
    writer.writerow(['Product Title', 'Product Link', 'Price Category', 'Price'])
    # loop through urls
    for url in urls:
        page = requests.get(url)
        soup = BeautifulSoup(page.content, 'html.parser')
        atags = soup.find_all('a', class_='product-item__link')
        # find all products in page
        for atag in atags:
            link = atag['href']
            title = atag.find('p', class_='product-item__title')
            price = atag.find('p', class_='product-item__price-wrapper')
            pricec = price.span.extract()
            writer.writerow([link, title.text, pricec.text, price.text.strip()])





""" print(link)
        print(title.text)
        print(pricec.text)
        print(price.text.strip())
        print() """