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
url = "https://www.gmarket.co.kr/n/best"
browser.get(url)
#time.sleep(3) # 페이지 로딩 대기

soup = BeautifulSoup(browser.page_source,"lxml")



data = soup.find("div",class_="box__best-list")
divs = data.find_all("div",class_="box__item-info")

print(divs[0].get_text())
print(len(divs))