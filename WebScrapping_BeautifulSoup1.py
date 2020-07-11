import requests
from bs4 import BeautifulSoup

# r=requests.get("http://www.edureka.co/")
r=requests.get("https://github.com/bitgrit-official/competition-platform/pull/504")
url = "https://www.amazon.com/Lenovo-ThinkPad-20QT001PUS-Mobile-Workstation/dp/B07TZ517ND/ref=sr_1_10?keywords=lenovo+i7+16gb+9th+generation&qid=1584684114&sr=8-10"

headers = {
    "User-Agent": 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36'
}
r=requests.get(url, headers=headers)
c=r.content
# print(c)

soup=BeautifulSoup(c,"html.parser")
print(soup.prettify())
# print(soup.prettify())

# links=[]

# # #All Links
# for link in soup.find_all('a'):
#     links.append(link.get('href'))

# print(links)

# All Spans by Class
# for price in soup.find_all('span',class_="after_discount"):
#     print(price)

price = soup.find(id="titleSection")
print(price)
