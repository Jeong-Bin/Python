
import requests
from bs4 import BeautifulSoup

for year in range(2015, 2020):  # 2015~2019년영화순위 페이지
    url = f"https://search.daum.net/search?w=tot&q={year}%EB%85%84%EC%98%81%ED%99%94%EC%88%9C%EC%9C%84&DA=MOR&rtmaxcoll=MOR"
    res = requests.get(url)
    res.raise_for_status()

    soup = BeautifulSoup(res.text, "lxml")

    images = soup.find_all("img", attrs={"class":"thumb_img"})

    for idx, image in enumerate(images): # idx, enumerate : 루프를 돌 때 인덱스가 0,1,2 로 돌아감
        # print(image["src"]) # 확인용
        # 확인해보니 https: 가 있는게 있고 없는게 있음
        image_url = image["src"]
        if image_url.startswith("//"):  # 만약 image_url이 // 로 시작한다면
            image_url = "https:" + image_url  # 앞에 https: 를 붙여라

        print(image_url)
        # 나온 url 페이지에 접속해서 그 이미지를 파일로 저장하기 위해 한 번 더 requests를 이용해 새롭게 접속
        image_res = requests.get(image_url) 
        image_res.raise_for_status()

        with open(f"movie_{year}_{idx+1}.jpg", "wb") as f:
            # {year}를 표시하지 않으면 앞으 년도꺼에 그대로 덮어쓰기 되어버림
            # 이미지는 글자가 아니기에 "wb"로 표시
            f.write(image_res.content) # image_res가 가진 content 정보(여기서는 이미지)를 파일로 저장

        if idx >= 4:  # 1~5위 영화 이미지만 다운로드
            break