import requests
from bs4 import BeautifulSoup
import csv

url = "https://search.daum.net/search?w=tot&q=2024%EB%85%84%EC%98%81%ED%99%94%EC%88%9C%EC%9C%84&DA=MOR&rtmaxcoll=MOR"
headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/136.0.0.0 Safari/537.36"}
res = requests.get(url,headers=headers)
res.raise_for_status()
print(res.text)

# 파싱
soup = BeautifulSoup(res.text,"lxml")

#with open("w0512/screen.html","w",encoding="utf-8") as f:
#    f.write(soup.prettify())
with open("w0512/screen.html","r",encoding="utf-8") as f:
    f.write(soup.prettify())

data = soup.find("div",id="morColl")
data2 = data.find("c-flicking")
# print(data2)
data3 = data2.find_all("c-doc")

print(data3[0].find("c-title"))
