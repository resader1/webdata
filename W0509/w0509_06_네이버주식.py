import requests
from bs4 import BeautifulSoup


url = "https://finance.naver.com/sise/sise_market_sum.naver"
headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/136.0.0.0 Safari/537.36 Edg/136.0.0.0"}
res = requests.get(url,headers=headers)
res.raise_for_status()
soup = BeautifulSoup(res.text,"lxml")

# print(soup.title)

# data = soup.find("div",class_="box_type_l")
# trs = data.tbody.find_all("tr")
# print(len(trs))
# print(trs[1])


# 6-10

data = soup.find("div",class_="box_type_l")
title = data.tbody.find_all("a",class_="title")
print(title)