#  requests : 웹상의 html 문서정보를 가져오는 라이브러리
# pip install  requests 

import requests
res = requests.get("http://naver.com")
print("응답코드 :", res.status_code) # 200 이면 정상