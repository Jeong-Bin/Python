# 코스피 시가 총액 순위(1위~200위)

import csv
import requests
from bs4 import BeautifulSoup

url = "https://finance.naver.com/sise/sise_market_sum.nhn?sosok=0&page="

# 마지막 단계
filemane = "시가총액1-200.csv"
f = open(filemane, "w", encoding="utf-8-sig", newline="") # newline="" : 자동 줄바꿈 안 함
writer = csv.writer(f)            # 한글이 깨진다면 뒤에 -sig 붙이기

# 추가 : 엑셀파일 맨 위에 컬럼명을 추가해줌
# 웹에서 컬럼을 복붙해옴
title = "N	종목명	현재가	전일비	등락률	액면가	시가총액	상장주식수	외국인비율	거래량	PER	ROE".split("\t")
print(type(title)) # 리스트로 잘 바꼈는지 화인
writer.writerow(title) # 리스트 형태로 넣기위해 split("\t")를 이용해 탭으로 구분된 데이터를 리스트 형태로 바꾼다.

for page in range(1, 5):
    res = requests.get(url + str(page))  # 1~4를 문자열로 바꿔서 url뒤에 붙여줌
    res.raise_for_status()
    soup = BeautifulSoup(res.text, "lxml")

    data_rows = soup.find("table", attrs={"class":"type_2"}).find("tbody").find_all("tr")
    for row in data_rows:
        columns = row.find_all("td")
        if len(columns) <= 1: # 아래 print로 확인한 줄바꿈용 1개짜리 td를 스킵함
            continue               # strip은 공백을 없앰
        data = [column.get_text().strip() for column in columns] # 한 줄 for문
        # columns 안의 값을 1개씩 가져와서 column으로 지정하고 거기에 get_text를 함
        #print(data) # 확인해보니 줄바꿈용 1개짜리 td들과 공백들(/n/n/t/t)이 있음
        
        writer.writerow(data)
        # writer.writerow 에 리스트 형태로 데이터를 넣어주면 되는데, data는 이미 리스트 형태[]니까 그대로 넣음