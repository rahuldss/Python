import requests
from bs4 import BeautifulSoup

r=requests.get("http://www.edureka.co/")
c=r.content
#print(c)

soup=BeautifulSoup(c,"html.parser")
#print(soup.prettify())

links=[]

# #All Links
# for link in soup.find_all('a'):
#     links.append(link.get('href'))

# print(links)

# All Spans by Class
for price in soup.find_all('span',class_="after_discount"):
    print(price)
