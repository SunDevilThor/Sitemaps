# Sitemaps
# Tutorial from John Watson Rooney YouTube channel

# To find a sitemap, input main url + /sitemap or /sitemap.xml
# You can also check the robots.txt file
# You can also search Google: site:website.com ext:xml

import requests
from bs4 import BeautifulSoup

url = 'https://www.winfieldsoutdoors.co.uk/sitemap_wf.xml/'

r = requests.get(url)

soup = BeautifulSoup(r.text, 'lxml')

links = soup.find_all('loc')

# print(len(links))

for link in links: 
    print(link.text)