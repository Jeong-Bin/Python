# 구글 무비 가져올 때 스크롤링 하면서 계속해서 로딩되는 영화들 가져오기

from selenium import webdriver
browser = webdriver.Chrome()
# browser.maximize_window

# 페이지 이동
url = "https://play.google.com/store/movies/top"
browser.get(url)

# 지정한 위치로 스크롤 내리기
# 해상도 높이인 1080 위치로 스크롤 내리기
# browser.execute_script("window.scrollTo(0, 1080)")  # 10810말고 다른것도 됨


# 화면 가장 아래로 스크롤 내리기
# 문서의 높이만큼 내림
browser.execute_script("window.scrollTo(0, document.body.scrollHeight)")

import time
interval = 2 # 2초에 한 번씩 스크롤 내림

# 현재 문서 높이를 가져와서 저장
prev_height = browser.execute_script("return document.body.scrollHeight")

# 반복 수행\
while True:
    # 스크롤 내리기
    browser.execute_script("window.scrollTo(0, document.body.scrollHeight)")
    
    # 로딩 대기
    time.sleep(interval)

    # 현재 문서 높이를 가져와서 저장 2
    curr_height = browser.execute_script("return document.body.scrollHeight")

    # 만약 현재 페이지 높이와 이전 페이지 높이가 같아지면 더이상 내릴게 없다는 뜻이므로 종료.
    if curr_height == prev_height:
        break

    # prev_height를 현재 페이지 높이로 업데이트 하고 재작업
    prev_height = curr_height

print("스크롤 완료")



# 15_selenium_movies 에서 사용한 코드를 가져 와서 수정

import requests
from bs4 import BeautifulSoup

soup = BeautifulSoup(browser.page_source, "lxml")                         

# 11위 부터는 class명이 Vpfmgd라서 리스트를 이용해 두 가지 class를 모두 불러온다.
# movies = soup.find_all("div", attrs={"class":["ImZGtf mpg5gc", "Vpfmgd"]})

# 그런데 확인해보니 1~10위는 class로 ImZGtf mpg5gc와 Vpfmgd 둘 다 가지고 있어서 값이 중복해서 2번 나왔다.
# 따라서 class는 Vpfmgd 하나만 불러오도록 한다.
movies = soup.find_all("div", attrs={"class": "Vpfmgd"})
print(len(movies)) # 영화를 몇 개 가져왔는지 확인용

# 영화 제목 가져오기
for movie in movies:
    title = movie.find("div", attrs={"class":"WsMG1c nnK0zc"}).get_text()
    # print(title)

# 할인하는 영화만 불러오기
    # 할인 전 가격    
    original_price = movie.find("span", attrs={"class":"SUZt4c djCuy"})
    if original_price:
        original_price = original_price.get_text()  # 할인 전 가격이 있으면(현재 할인 중이라면) 그걸 불러온다.
    else:
        print(title, " <할인되지 않은 영화 제외>")
        continue

    # 할인 후 가격
    price = movie.find("span", attrs={"class":"VfPpfd ZdBevf i5DZme"})

    # 링크(a 태그 찾아서 class명 확인)
    link = movie.find("a", attrs={"class":"JC71ub"})["href"]
    # 올바른 링크 : https://play.google.com + link