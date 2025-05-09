import requests


# url = 'https://www.melon.com/'
url = 'https://www.google.com/'
# url = 'https://www.whatismybrowser.com/detect/what-is-my-user-agent/'
headers = {"user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/136.0.0.0 Safari/537.36 Edg/136.0.0.0"}
# user-agent : python-requests/
res = requests.get(url,headers=headers)
res.raise_for_status() # 에러시 종료
print(res.text) 
with open("W0509.test.html","w",encoding="utf8") as f:
    f.write(res.text)
print("[프로그램 종료]")
# if res.status_code == 200:
#     print("정상적인 프로그램 진행")
#     print(res)
    
#     print("응답코드 : ",res.status_code) 
   
#     print(res.text) 
#     print("[프로그램 종료]")
# else:
#     print("프로그램 종료")
#     res.raise_for_status() 
