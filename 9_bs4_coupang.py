# 쿠팡 - 노트북
import requests
import re
from bs4 import BeautifulSoup

url = "https://www.coupang.com/np/search?q=%EB%85%B8%ED%8A%B8%EB%B6%81&channel=user&component=&eventCategory=SRP&trcid=&traid=&sorter=scoreDesc&minPrice=&maxPrice=&priceRange=&filterType=&listSize=36&filter=&isPriceRange=false&brand=&offerCondition=&rating=0&page=1&rocketAll=false&searchIndexingToken=&backgroundColor="
headers = {"User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36"}
res = requests.get(url, headers=headers)
res.raise_for_status()
soup = BeautifulSoup(res.text, "lxml")

# li 태그 중에서 class가 search-product로 시작하는 모든 엘리먼트를 가져와라
items = soup.find_all("li", attrs={"class":re.compile("^search-product")})
# items 변수로 가져온 것 중 첫 번째 엘리먼트의 name을 출력하라
# print(items[0].find("div", attrs={"class":"name"}).get_text())

for item in items:
    name = item.find("div", attrs={"class":"name"}).get_text()  # 제품명
    price = item.find("strong", attrs={"class":"price-value"}).get_text()  # 가격
    
    rate = item.find("em", attrs={"class":"rating"})  # 평점
    if rate:
        rate = rate.get_text()
    else:
        rate = "평점 없음"

    rate_cnt = item.find("span", attrs={"class":"rating-total-count"})  # 평점 수
    if rate_cnt:
        rate_cnt = rate_cnt.get_text()
    else:
        rate_cnt = "평점 수 없음"
    print(name, price, rate, rate_cnt)