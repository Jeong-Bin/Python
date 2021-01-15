# 쿠팡 - 노트북
import requests
import re
from bs4 import BeautifulSoup

headers = {"User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36"}

# 최근 다섯 페이지에서 스크래핑
for i in range(1, 6):
    print("페이지 :", i)
    # 페이지 넘어가는건 f-string 을 활용
    url = f"https://www.coupang.com/np/search?q=%EB%85%B8%ED%8A%B8%EB%B6%81&channel=user&component=&eventCategory=SRP&trcid=&traid=&sorter=scoreDesc&minPrice=&maxPrice=&priceRange=&filterType=&listSize=36&filter=&isPriceRange=false&brand=&offerCondition=&rating=0&page={i}&rocketAll=false&searchIndexingToken=&backgroundColor="
    
    res = requests.get(url, headers=headers)
    res.raise_for_status()
    soup = BeautifulSoup(res.text, "lxml")

    # li 태그 중에서 class가 search-product로 시작하는 모든 엘리먼트를 가져와라
    items = soup.find_all("li", attrs={"class":re.compile("^search-product")})

    for item in items:

        # 광고 제품 제외   
        ad_badge = item.find("span", attrs={"class":"ad-badge-text"})
        if ad_badge:
            # print(" <광고 상품 제외합니다.>")
            continue

        name = item.find("div", attrs={"class":"name"}).get_text()  # 제품명

        # Apple 제품 제외
        if "Apple" in name:
            # print(" <Apple 상품 제외합니다>")
            continue

        price = item.find("strong", attrs={"class":"price-value"}).get_text()  # 가격

        rate = item.find("em", attrs={"class":"rating"})  # 평점
        if rate:
            rate = rate.get_text()
        else:
            rate = "평점 없음"
            # print(" <평점 없는 상품 제외합니다>")
            continue

        rate_cnt = item.find("span", attrs={"class":"rating-total-count"})  # 평점 수
        if rate_cnt:
            rate_cnt = rate_cnt.get_text()[1:-1]  # 예 : (26)
                                                # 슬라이싱으로 2번째 값 ~ 뒤에서 2번째 값만 뽑아내기

        else:
            rate_cnt = "평점 수 없음"
            # print(" <평점 수 없는 상품 제외합니다>")
            continue

        # 제품 링크 가져오기
        link = item.find("a", attrs={"class":"search-product-link"})["href"]

        # 평점 4.5이상, 리뷰 100개 이상만 조회.
        # 일단 rate를 float 형태로, rate_cnt는 int 형태로 바꿔줌
        if float(rate) >= 4.5 and int(rate_cnt) >= 100:
            #print(name, price, rate, rate_cnt)
            print(f"제품명 : {name}")
            print(f"가격 : {price}")
            print(f"평점 : {rate}점 ({rate_cnt})개")
            print(f"바로가기 : https://www.coupang.com{link}")
            print("-"*50) # 구분선
