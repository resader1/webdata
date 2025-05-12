from selenium import webdriver
from bs4 import BeautifulSoup
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time
import requests
# 크롬 옵션 설정
options = Options()
options.add_argument("--disable-blink-features=AutomationControlled")  # 자동화 티 안 나게
options.add_argument("start-maximized")
options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36")
options.add_experimental_option("excludeSwitches", ["enable-automation"])
options.add_experimental_option('useAutomationExtension', False)
# 브라우저 실행
browser = webdriver.Chrome(options=options)
# 쿠팡 페이지 접속
url = "https://www.melon.com/chart/index.htm"
browser.get(url)

soup = BeautifulSoup(browser.page_source,"lxml")
###
data = soup.find("tbody")
trs = data.find_all("tr")

tds = trs[0].find_all("td")
print(tds[1].find("span",{"class":"rank"}).get_text().strip())
print(tds[3].img["src"])
imgUrl = tds[3].img["src"]
img_res = requests.get(imgUrl)
with open("w0512/melon_chart1.jpg","wb") as f:
    f.write(soup.prettify())
print(tds[6].find("a").get_text().strip())
cnt = int(tds[7].find("span",{"class":"cnt"}).get_text().strip()[3:].strip().replace(",",""))
### 천단위 표시 제거, int타입으로 변경
print(cnt)


input("종료시 enter")