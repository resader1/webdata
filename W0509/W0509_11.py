import requests
from bs4 import BeautifulSoup
import csv

with open("w0509/join02_info_input.html","r",encoding="utf8") as f:
    soup = BeautifulSoup(f,"lxml")
    
ff = open("w0509/fff.csv","w",encoding="utf-8-sig",newline="")
writer = csv.writer(ff) # csv List 타입 저장

data = soup.find_all("fieldset")
for d in data:
    fileName = []
    dts = d.find_all("dt")
    for dt in dts:
        print(dt.get_text().strip(), end='\t')  # 공백제거 strip()
        fileName.append(dt.get_text().strip())
    writer.writerow(fileName)
ff.close()
print("저장완료")

# data = soup.find_all("dt")
# print(data)
# fileName = []
# for dt in data:
#     print(dt.get_text(),end="\t")
#     fileName.append(dt.get_text())
# writer.writerow(fileName)
# print()
