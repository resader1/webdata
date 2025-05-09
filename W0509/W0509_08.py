import requests
from bs4 import BeautifulSoup

# html 파일을 읽어와서 파일 html,css 형태로 파싱
with open("w0509/게시판3.html","r",encoding="utf8") as f:
    soup = BeautifulSoup(f,"lxml")
    

# html 태그로 찾는 방법
# print(soup.thead)
# soup.find("thead",class_="")
data = soup.find("thead")    
print(data.find_all("th")[0].get_text())
ths = data.find_all("th")
for th in ths:
    print(th.get_text()[0])

# 자바를 못읽음..
print("*"*80)
data = soup.find("tbody",id="tbody")
trs = data.find_all("tr")
# print(len(trs))

for tr in trs:
    tds = tr.find_all("td")
    
    if len(tds)>1:
        for i in range(len(tds)-1):
            print(tds[i].get_text(),end="\t")
            print()
                
            
            # print(td.get_text())
    # print(len(tds))

## find_next_sibling - 이후형제 찾기, find_previous_sibling - 이전형제 찾기  
# data = soup.find("div",{"id":"input"})
# data2 = data.find_next_Sibling()
# print(data2)

# print(data.div.get_text())



