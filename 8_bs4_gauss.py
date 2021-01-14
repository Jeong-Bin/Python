import requests
from bs4 import BeautifulSoup

# 웹툰 가우스 전자

url = "https://comic.naver.com/webtoon/list.nhn?titleId=675554"
res = requests.get(url)
res.raise_for_status()  # 혹시나 문제가 생기면 프로그램 종료

soup = BeautifulSoup(res.text, "lxml")
# cartoons = soup.find_all("td", attrs={"class":"title"})
# # 일단 테스트 용으로 한 개만 가져오기
# title = cartoons[0].a.get_text()
# link  = cartoons[0].a["href"]
# print(title)
# print("https://comic.naver.com"+link)

# # 반복문 활용해서 제목과 링크 가져오기
# for cartoon in cartoons:
#     title = cartoon.a.get_text()
#     link  = "https://comic.naver.com" + cartoon.a["href"]
#     print(title, link)

# 최근 10개 화의 평점 구하기
total_rates = 0
cartoons = soup.find_all("div", attrs={"class":"rating_type"})
for cartoon in cartoons:
    rate = cartoon.find("strong").get_text()
    print(rate)
    total_rates += float(rate)
print("전체 점수 : ", total_rates)
print("평균 점수 : ", total_rates / len(cartoons))