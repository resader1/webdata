import requests
from bs4 import BeautifulSoup


with open("W0509/a.html","r",encoding="utf8") as f:
    soup = BeautifulSoup(f,"lxml")

# print(soup.title)    
# print(soup.title.get_text())
# print(soup.h2)
# print(soup.find_all("h2"))
# print(soup.find("p",id="p1").get_text())


# print(soup.find("ul"))
# print("-"*80)
# print(soup.find("div",class_='c2').find("ul"))



# print("-"*80)

# print(soup.find("div",class_="c1").find("ul").find_all("li")[1].get_text())


print("-"*80)

print(soup.find("div",class_="c2").find("ul").get_text())
# url = ""
# headers = ""
# res = requests(url,geaders=headers)
# soup = BeautifulSoup("w0509/a.html","lxml")
# print(soup)