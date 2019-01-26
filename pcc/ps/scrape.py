import requests
from pprint import pprint
from bs4 import BeautifulSoup

sauce = 'http://m.ironman.com/triathlon/events/americas/ironman/world-championship/results.aspx'

r = requests.get(sauce)
data = r.text

soup = BeautifulSoup(data, 'html.parser')

print(soup.title.string)
print(soup.tr)
print(soup.tbody)

# Moving to the next page function

'''
counter = 1

while (counter <= 100):
    for post in posts:

        # Getting the title, author, ...
        # Writing to CSV and incre,enting counter...

    next_button = soup.find("span",class_="next-button")
    next_page_link = next_button.find("a").attrs['href']
    time.sleep(2)
    page = requests.get(((next_poage_link, headers=headers)
    soup = BeautifulSoup(page.text, 'html.parser')
''' 
