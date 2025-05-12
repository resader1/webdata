import requests
from bs4 import BeautifulSoup
import csv

url = "https://finance.naver.com/sise/sise_market_sum.naver?&page=1"
headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/136.0.0.0 Safari/537.36"}
res = requests.get(url,headers=headers)
res.raise_for_status()

# 파싱
soup = BeautifulSoup(res.text,"lxml")

### 파일저장
ff = open("w0512/stoce.csv","w",encoding="utf-8-sig",newline="")
writer = csv.writer(ff)

title = []
tdata = soup.find('thead')
ths = tdata.find_all("th")
for th in ths[:-1]:
    title.append(th.get_text().strip())

writer.writerow(title)

data = soup.find("tbody")
print(data)
print("*"*80)
trs = data.find_all("tr")

for tr in trs:
    tds = tr.find_all("td")
    contents = []
    if len(tds) <= 1:
        continue
    
    for i,td in enumerate(tds):
        if i==3:
            em1 = td.find("em").get_text().strip()
            span1 = td.find("span",class_="tah").get_text().strip()
            contents.append(em1+span1)
            print(em1+span1)
            continue
        tcontent = td.get_text().strip()
    contents.append(tcontent)
    print(tcontent)
    print("-"*80)


    
# 현재가 전체 합계 계산

sum = 0
for tr in trs:
    tds = tr.find_all("td")
    
    if len(tds) <= 1:
        continue
    
    elif i == 12:break
    number = td.get_text().strip()
    contents.append(number)
    pri = number.replace(",", "")
    
    sum += int(pri)
            
        

print("-"*80)
print(sum)
print(print(f"{sum:,}"))



# print("*"*80)
# print(trs[1])
# print(trs[2])


# #td 여러개
# tds = trs[1].find_all("td")
# for td in tds:
#     print(td.get_text().strip())
# print("-"*80)
# tds = trs[2].find_all("td")
# for td in tds:
#     print(td.get_text().strip())
# print("-"*80)
# tds = trs[3].find_all("td")
# for td in tds:
#     print(td.get_text().strip())
# print("-"*80)










# data = soup.find("thead")
# print(data)

# print("8"*80)
# ths = data.find_all("th")
# for th in ths:
#     print(th.get_text())
    
# print(ths[4].get_text())