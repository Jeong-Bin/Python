import requests
from bs4 import BeautifulSoup

# 웹툰 가우스 전자

url = "https://comic.naver.com/webtoon/list.nhn?titleId=675554"
res = requests.get(url)
res.raise_for_status()  # 혹시나 문제가 생기면 프로그램 종료

soup = BeautifulSoup(res.text, "lxml")
cartoons = soup.find_all("td", attrs={"class":"title"})
# 일단 테스트 용으로 한 개만 가벼오기
# title = cartoons[0].a.get_text()
# link  = cartoons[0].a["href"]
# print(title)
# print("https://comic.naver.com"+link)

# 반복문 활용
for cartoon in cartoons:
    title = cartoon.a.get_text()
    link  = "https://comic.naver.com" + cartoon.a["href"]
    print(title, link)