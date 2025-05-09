import requests
from bs4 import BeautifulSoup

# url = 'https://finance.naver.com/sise/sise_market_sum.naver'
url = 'https://n.news.naver.com/article/011/0004483132?ntype=RANKING'

headers = {"user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/136.0.0.0 Safari/537.36 Edg/136.0.0.0"}
res = requests.get(url,headers=headers)
res.raise_for_status()
# print(res.text)
# 문자열 -> html,css파싱
soup = BeautifulSoup(res.text,"lxml")
# print(soup)  # html,css
# <title>태그에 접근해서 가져옴
# print(soup.title)
# print(soup.title.get_text())
# print(soup.header)
# print(soup.header.div)
# print(soup.header.div.a)
## 태그 속성을 출력
# print(soup.header.div.a.attrs) # 속성의 전체 출력
# print(soup.header.div.a['href']) # 해당 속성값 1개 출력
# print(soup.header.div.a['class']) # 해당 속성값 1개 출력

## id,class 속성 출력
# find() 해당태그를 검색할 때 사용

# data1 = soup.find("a",attrs={"class":"ofhd_float_back"})
# print(data1)
# data1 = soup.find("a",{"class":"ofhd_float_back"})
# print(data1)
# data1 = soup.find("a",class_="ofhd_float_back")
# print(data1)


# data2 = soup.find("h2",attrs={"id":"title_area"})
# print(data2)
# print(data2.get_text())
# data2 = soup.find("h2",{"id":"title_area"})
# print(data2.get_text())
# data2 = soup.find("h2",id="title_area")
# print(data2.get_text())

### find() 1개만 검색, find_all() 복수개를 검색
ul_data = soup.find("ul",class_="ranking_list")
# li_data = ul_data.find("li",class_="rl_item")
li_datas = ul_data.find_all("li",class_="rl_item")
print(len(li_datas))
print(li_datas)
for li_data in li_datas:
    print(li_data.find("p",class_="rl_txt").get_text())
    
    