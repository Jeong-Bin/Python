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
