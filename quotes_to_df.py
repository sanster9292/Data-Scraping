# This is a practice scirpt for web scraping
# I will be scraping a website which is meant to be scraped as a practice.
# I am trying to use this to up my data engineering skills and get more acquaineted
# with collecting data online without any manual input.

#libraries
from bs4 import BeautifulSoup as bs
import requests
import pandas as pd


# Base URL
start_url = 'http://quotes.toscrape.com'


# This will read in the url using requests and change it into a
# BeautifulSoup structure

def get_web_soup(url):

    req_url = requests.get(url)
    web_soup = bs(req_url.content, 'html.parser')

    return web_soup

# This will parse the soup structure and isolate classes wheose name is quote

def scrape_the_page(web_soup):
    divs = web_soup.findAll('div', attrs = {"class": "quote"})
    authors_list = []

    for div in divs:
        text = div.find('span', attrs = {"class":"text"}).text.strip()
        author = div.find('small', attrs ={'class':'author'}).text.strip()

        text_author = (author, text)
        authors_list.append(text_author)
    return authors_list

# So far this website has 10 pages so I am going to parse these through using a
# for loop

def new_page_num(start_url):
    new_url = start_url+'/page/'


    return new_url

# Let's bring it all together
def main():
    start_url = 'http://quotes.toscrape.com'
    author_quotes = []

    start_soup = get_web_soup(start_url)
    page_1 = scrape_the_page(start_soup)
    author_quotes += page_1

    for page in range(2,11):
        page_stump = start_url+'/page/'
        new_url = page_stump+str(page)

        new_soup = get_web_soup(new_url)
        page_n = scrape_the_page(new_soup)
        author_quotes += page_n

    return author_quotes

# Let's create a Pandas dataframe to store all the Authors and their associated author_quotes
# This will make it more friendly for use

quotes = main()

df_authors = pd.DataFrame(quotes, columns = ['Author', 'Quote'])
df_authors.sample(10)
