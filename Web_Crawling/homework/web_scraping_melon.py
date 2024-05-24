from selenium import webdriver
from bs4 import BeautifulSoup
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

user = "Mozilla/5.0 (IPhone; CPU iPhone OS 13_3 like Mac OS X) AppleWebKit/605.1.15(KHTML, like Gecko) CriOS/80.0.3987.95 Mobile/15E148 Safari/604.1"

options_ = Options()
options_.add_argument(f"user-agent={user}")
# options_.add_experimental_option("detach", True)

options_.add_experimental_option("excludeSwitches", ["enable-logging"])


#크롬 드라이버 매니저를 자동으로 설치되도록 실행시키는 코드
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=options_)

url = "https://m2.melon.com/index.htm"
driver.get(url)
time.sleep(0.5)

def check_and_pass_event_page() :
    # #이벤트 페이지 넘어가기
    # 이벤트 페이지면 호출
    try : 
        driver.find_element(By.CLASS_NAME, 'ir-pm')
        print('Delete AD')
        driver.find_element(By.XPATH, '/html/body/div[2]/header/h1/a/img').click() #멜론 로고 클릭
        
    except :
        pass
    
check_and_pass_event_page()

def scroll_down_inf() :
    check_and_pass_event_page()
    time.sleep(1)
    #끝까지 스크롤 하기
    prev_height = -1
    max_scrolls = 100
    scroll_count = 0
    while scroll_count < max_scrolls:
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(1)  # give some time for new results to load
        new_height = driver.execute_script("return document.body.scrollHeight")
        if new_height == prev_height:
            break
        prev_height = new_height
        scroll_count += 1
    time.sleep(1)
    check_and_pass_event_page()
    
    
driver.find_element(By.XPATH, '//*[@id="naviMenu"]/nav/ul/li[3]/a').click()#차트 항목 클릭
scroll_down_inf()# 끝까지 스크롤 내리기

driver.find_element(By.XPATH,'/html/body/div[1]/div/div/article[3]/button').click() # 더보기 클릭

scroll_down_inf()#끝까지 스크롤 내리기
    

#아래 순서대로 스크래핑한 자료를 출력해주세요
#순위 :
#노래 제목 :
#가수 이름 :
for i in driver.find_element(By.ID, '_chartList').find_elements(By.CLASS_NAME,'list_item') :
    print('순위 : ',i.find_element(By.CLASS_NAME, 'ranking_num').text.split('\n')[0])
    print('노래 제목 : ',i.find_element(By.CLASS_NAME,'content').text.split('\n')[0])
    print('가수 이름 : ',i.find_element(By.CLASS_NAME,'content').text.split('\n')[1])






driver.quit()