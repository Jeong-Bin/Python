# 네이버 항공권

from selenium import webdriver
browser = webdriver.Chrome()
browser.maximize_window()  # 창 최대화

url = "https://flight.naver.com/flights/"
browser.get(url)  # url로 이동

# "가는날 선택" 클릭
browser.find_element_by_link_text("가는날 선택").click()

# 이번달 27일(가는날), 28일(오는날) 선택
#browser.find_elements_by_link_text("27")[0].click() # 모든 27 중 첫 번째 선택
#browser.find_elements_by_link_text("28")[0].click()

# 다음달 27일(가는날), 28일(오는날) 선택
#browser.find_elements_by_link_text("27")[1].click() # 모든 27 중 두 번째 선택
#browser.find_elements_by_link_text("28")[1].click()

# 이번달 27일(가는날), 다음달 28일(오는날) 선택
browser.find_elements_by_link_text("27")[0].click() 
browser.find_elements_by_link_text("28")[1].click()

# 제주도 여행 베너에서 copy xpath. 이 때는 a 태그가 아닌 그 상위에 있는 li 태그를 복사해야 잘 동작함
browser.find_element_by_xpath("//*[@id='recommendationList']/ul/li[1]").click()

# "항공권 검색 클릭"
browser.find_element_by_link_text("항공권 검색").click()

# 첫 번째 결과 출력
elem = browser.find_element_by_xpath("//*[@id='content']/div[2]/div/div[4]/ul/li[1]")
print(elem.text)