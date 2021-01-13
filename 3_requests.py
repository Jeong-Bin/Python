import requests
res = requests.get("http://naver.com")
print("응답코드 :", res.status_code) # 200 이면 정상