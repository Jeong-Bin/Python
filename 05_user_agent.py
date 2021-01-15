import requests
url = "http://nadocoding.tistory.com"
# 구글에 What is my user agent 라고 검색해서 내 user agent를 복사해온다.
headers = {"User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36"}
res = requests.get(url, headers=headers)
print("응답코드 :", res.status_code) # 200 이면 정상

# 새로운 html 파일을 만들어서 위 페이지의 모든 코드를 넣음
with open("nadocoding.html", "w", encoding="utf-8") as f:
    f.write(res.text)


