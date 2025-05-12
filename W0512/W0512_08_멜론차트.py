import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import csv
import time
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
#time.sleep(3) # 페이지 로딩 대기

soup = BeautifulSoup(browser.page_source,"lxml")


### 1-100등
# 순위 가수   곡명             좋아요        이미지링크
# 1    10cm  너에게 닿기를

data = soup.find("tbody")
trs = data.find_all("tr")

## 파일 저장
ff = open("w0512/melon1.csv","w",encoding="utf-8-sig",newline="")
writer = csv.writer(ff)
### 타이틀
title = ["순위","곡제목","가수","좋아요"]
writer.writerow(title)


### 1-100 순위까지 저장
for tr in trs:
    cont = []
    tds = tr.find_all("td")
    # 순위
    rank = tds[1].find("span",{"class":"rank"}).get_text()
    cont.append(rank)
    print(rank)
    # 제목
    song = tds[5].find("div",{"class":"rank01"}).a.get_text()
    print(song)
    #가수
    singer = tds[5].find("div",{"class":"rank02"}).a.get_text()
    print(singer)
    #좋아요
    cnt = tds[7].find("span",{"class":"cnt"}).get_text().strip()[3:].strip()

    cnt = int(cnt.replace(",",""))
    print(cnt)
    print(tds[3].img["src"])
    
    cont = [rank,song,singer,cnt]
    writer.writerow(cont)
    
    imgUrl = tds[3].img["src"]
    img_res = requests.get(imgUrl)
    with open(f"w0512/images/melon_chart{rank}.jpg","wb") as f:
        f.write(img_res.content)
    
    
    
    
        
    
        
        
### csv
ff.close()
        

print("프로그램 종료")