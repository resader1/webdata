import requests
from bs4 import BeautifulSoup
import csv

# html 파일을 읽어와서 파일 html,css 형태로 파싱
with open("w0509/게시판3.html","r",encoding="utf8") as f:
    soup = BeautifulSoup(f,"lxml")
    
# html태그 출력 soup.title
print(soup.title)
print(soup.title.get_text())

# 속성 출력 soup.a['href]
print(soup.a['href'])

# find(),find_all()

data = soup.find("thead")
ths = data.find_all("th")
print("th개수 : ",len(ths))




#파일 저장
fileName = "board.csv"
ff = open("w0509/"+fileName,"w",encoding="utf-8-sig",newline="")
writer = csv.writer(ff)



#상단제목 파일에 저장
topTitle = []
for i,th in enumerate(ths):
    if i<5:
        print(th.get_text(),end="\t")
        topTitle.append(th.get_text())
writer.writerow(topTitle)
print()

print("-"*80)



data2 = soup.find("tbody")
trs = data2.find_all("tr")
for tr in trs:
    tds = tr.find_all("td")
    if len(tds)<=1:continue
    bodyData = [] #게시글 부분 데이터 저장
    for i,td in enumerate(tds):
        if i<5:
            print(td.get_text(),end="\t")
            bodyData.append(td.get_text())
    writer.writerow(bodyData) # 파일에 게시글 1개를 저장
            
    print()
    
    
print("저장완료")
    
    
    