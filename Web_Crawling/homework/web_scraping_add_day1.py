import requests
from bs4 import BeautifulSoup

header_user = {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"}

url = "http://www.cgv.co.kr/movies/?lt=1&ft=0"

req = requests.get(url, headers=header_user)

html = req.text
soup = BeautifulSoup(html, "html.parser")
ranks = soup.select('.rank')
titles = soup.select('.title')
percents = soup.select('.percent')
txt_infos = soup.select('.txt-info')

for rank, title, percent, txt_info in zip(ranks, titles, percents, txt_infos):
    print('순위 : ',rank.text.strip().replace('No.', ''),'\n',\
        '제목 : ', title.text.strip(),'\n',\
            '예매율 : ',percent.text.strip().replace('에매율',''),'\n',\
                '개봉일 : ',txt_info.text.strip().replace('개봉', ''))



