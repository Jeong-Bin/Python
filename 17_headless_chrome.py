# headless chrome : 크롬창을 일일이 띄우지 않고 백그라운드에서만 작동하도록 함.
# -> 속도가 더 빨라짐
# 16_selenium_movies_scroll 파일을 그대로 사용

from selenium import webdriver

# <headless chrome>
options = webdriver.ChromeOptions()
options.headless = True
options.add_argument("Window-size=1920x1080")  # 눈에 보이지는 않지만 내부적으로 이 크기의 브라우저를 띄움

                           # 위의 options를 넣어주면 끝! 추가적으로 스크린샷 기능도 있음. 그건 아래에!
browser = webdriver.Chrome(options=options)
browser.maximize_window

url = "https://play.google.com/store/movies/top"
browser.get(url)

browser.execute_script("window.scrollTo(0, document.body.scrollHeight)")

import time
interval = 2 

prev_height = browser.execute_script("return document.body.scrollHeight")


while True:
    
    browser.execute_script("window.scrollTo(0, document.body.scrollHeight)")
    
    time.sleep(interval)

    curr_height = browser.execute_script("return document.body.scrollHeight")

    if curr_height == prev_height:
        break

    prev_height = curr_height

print("스크롤 완료")

#################################################
# 눈에 보이진 않지만 스크린샷을 찍어서 파일로 저장할 수 있음
# 이걸 통해 잘 동작했는지 확인 가능
browser.get_screenshot_as_file("google_movie.png")


import requests
from bs4 import BeautifulSoup

soup = BeautifulSoup(browser.page_source, "lxml")                         


movies = soup.find_all("div", attrs={"class": "Vpfmgd"})
print(len(movies)) 


for movie in movies:
    title = movie.find("div", attrs={"class":"WsMG1c nnK0zc"}).get_text()

    original_price = movie.find("span", attrs={"class":"SUZt4c djCuy"})
    if original_price:
        original_price = original_price.get_text() 
    else:
        continue

    price = movie.find("span", attrs={"class":"VfPpfd ZdBevf i5DZme"}).get_text()

    link = movie.find("a", attrs={"class":"JC71ub"})["href"]

    print(f"제목 : {title}")
    print(f"할인 전 금액 : {original_price}")
    print(f"할인 후 금액 : {price}")
    print("링크 :", "https://play.google.com" + link)
    print("-" * 55)

browser.quit()