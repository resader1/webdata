import requests
from bs4 import BeautifulSoup
import csv

with open("w0509/notice_list.html","r",encoding="utf8") as f:
    soup = BeautifulSoup(f,"lxml")
    
    
### table -> tr

# data = soup.find("table")
# ths = data.find_all("th")
# for th in ths:
#     print(th.get_text())


print("-"*80)


# data2 = soup.find("tbody")
# trs = data.find_all("tr")
# for i,tr in enumerate(trs):
#     if i%2 != 1:
#         print(tr.get_text())
ff = open("w0509/list.csv","w",encoding="utf-8-sig",newline="")
writer = csv.writer(ff) # csv List 타입 저장

trs = soup.table.find_all("tr")
print(len(trs))

for i,tr in enumerate(trs):
    fileName = []
    if i == 0: 
        data = soup.find("table")
        ths = data.find_all("th")
        for th in ths:
            print(th.get_text(),end="\t")
            fileName.append(th.get_text())
            
        writer.writerow(fileName) # 상단 타이틀 List 타입으로 저장
        print()
        continue
    tds = tr.find_all("td")
    for td in tds:
        print(td.get_text(),end="\t")
        fileName.append(td.get_text())
    print()
    writer.writerow(fileName) # 내용부분 List 타입으로 저장
    
    
print("저장 완료")