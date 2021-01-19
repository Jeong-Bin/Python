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

# 첫 번째 결과 출력.  이 방법은 로딩 때문에 안 됨
# elem = browser.find_element_by_xpath("//*[@id='content']/div[2]/div/div[4]/ul/li[1]")
# print(elem.text)


# 중간 로딩시간 때문에 로딩 기다린 후 로딩이 끝나면 이후 코드가 작동하도록 해야함
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# 브라우저를 최대 10초를 기다리되, 다음 엘리먼트가 나오면 바로 진행
# 만약 10초가 지나도 로딩이 안 끝나면 에러가 나기때문에 그냥 끝내도록 함. -> try:, finally: 사용 
try:
    elem = WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.XPATH, "//*[@id='content']/div[2]/div/div[4]/ul/li[1]")))
                                                                            # XPATH 외에도 ID, CLASS_NAME, LINK_TEXT 등도 사용 가능함
    print(elem.text)  # 첫 번째 항공편 결과를 터미널로 출력

finally:
    browser.quit()

