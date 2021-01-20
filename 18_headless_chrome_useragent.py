
from selenium import webdriver


options = webdriver.ChromeOptions()
options.headless = True
options.add_argument("Window-size=1920x1080")  

# headless chrome 사용시 주의사항
# 만약 아래처럼 자신의 user-agent를 명시하지 않으면 HeadlessChrome으로 표기되면서 서버에서 접속을 막을 수도 있음
options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36")

browser = webdriver.Chrome(options=options)
browser.maximize_window

url = "https://www.whatismybrowser.com/detect/what-is-my-user-agent"
browser.get(url)

detected_value = browser.find_element_by_id("detected_value")
print(detected_value.text)
browser.quit()
