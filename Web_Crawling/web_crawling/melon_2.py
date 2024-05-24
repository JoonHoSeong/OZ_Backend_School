import requests
from bs4 import BeautifulSoup

header_user = {"User-Agent" : "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.163 Safari/537.36"}

base_url = 'https://www.melon.com/chart/index.htm'

req = requests.get(base_url, headers=header_user)
html = req.text
soup = BeautifulSoup(html,"html.parser")

print(html)
# print(soup.h1)

# logo = soup.find(class_= 'ui-autocomplete-input')
# print(logo)