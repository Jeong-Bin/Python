# pip install beautifulsoup4
# pip install lxml

import requests
from bs4 import BeautifulSoup

url =  "https://comic.naver.com/webtoon/weekday.nhn"
res = requests.get(url)
res.raise_for_status()  # 혹시나 문제가 생기면 프로그램 종료

soup = BeautifulSoup(res.text, "lxml")

print(soup.title)  # title을 가져옴
print(soup.title.get_text())  # title의 text만 가져옴
print(soup.a)  # 첫 번째 a 태그를 가져옴
print(soup.a.attrs)  # 첫 번째 a 태그의 속성들을 가져옴
print(soup.a["href"])  # 특정 속성에 대한 정보를 가져옴
# 위 방법들은 해당 페이지에 대해 잘 알고 있을 때 사용할 수 있다.

# find를 사용해 특정 정보에 해당하는 값 중에 처음으로 발견되는 엘리먼트를 가져올 수 있음
print(soup.find("a", attrs={"class":"Nbtn_upload"}))  # class가 "Nbtn_upload" 인 a element를 찾아줘
print(soup.find(attrs={"class":"Nbtn_upload"}))  # class가 "Nbtn_upload" 인 어떤 element를 찾아줘



rank1 = soup.find("li", attrs={"class":"rank01"})
print(rank1.a.get_text())
rank2 = rank1.next_sibling.next_sibling 
# next_sibling을 통해 형제관계에 있는 다음 엘리먼트로 넘어갈 수 있다.
# 두 번 한 이유는 중간에 줄바꿈 등이 있어서.
rank3 = rank2.next_sibling.next_sibling
print(rank3.a.get_text())
rank2 = rank3.previous_sibling.previous_sibling # next의 반대는 previous
print(rank2.a.get_text())

print(rank1.parent)  # rank1의 부모로 이동

rank2 = rank1.find_next_sibling("li") # 조건에 해당하는 엘리먼트만 찾음. 따라서 위 처럼 두 번 적을 필요가 없음
rank3 = rank2.find_next_sibling("li")
rank2 = rank3.find_previous_sibling("li")
print(rank2.a.get_text())
print(rank3.a.get_text())
print(rank2.a.get_text())

# sibling's'라고 하면 다음에 나오는 정보를 모두 가져옴
print(rank1.find_next_siblings("li"))


# 텍스트 기준으로 찾기
webtoon = soup.find("a", text="독립일기-56화 온라인 신년회")
print(webtoon)
