import requests
from bs4 import BeautifulSoup

header_user = {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"}

base_url = "https://search.naver.com/search.naver?ssc=tab.blog.all&sm=tab_jum&query="
# keyword = input("검색어를 하나만 입력해주세요 : ")
keyword = '유산균'

url = base_url + keyword
req = requests.get(url, headers=header_user)

html = req.text
soup = BeautifulSoup(html, "html.parser")

# 스크롤 없이 현재 페이지의 정보만 받아옴
blogs = soup.select(".view_wrap")
for blog in blogs :
    if blog.select(".link_ad") :
        continue
    title = blog.select_one(".title_area").text
    writer = blog.select_one(".user_info").select_one('.name').text
    print('검색 키워드 : ', keyword)
    print('블로그 제목 : ',title)
    print('블로그 작성자 : ', writer, '\n')
