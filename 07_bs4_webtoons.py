# 네이버 웹툰 스크래핑
import requests
from bs4 import BeautifulSoup

url =  "https://comic.naver.com/webtoon/weekday.nhn"
res = requests.get(url)
res.raise_for_status()  # 혹시나 문제가 생기면 프로그램 종료

soup = BeautifulSoup(res.text, "lxml")

# 네이버 웹툰 전체 목록 가져오기
cartoons = soup.find_all("a", attrs={"class":"title"})  # find_all 조건에 해당하는 모든 태그 찾음
# class 속성이 title인 모든 a element 반환
for cartoon in cartoons:
    print(cartoon.get_text())