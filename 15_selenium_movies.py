# 구글 무비

import requests
from bs4 import BeautifulSoup

url = "https://play.google.com/store/movies/top"

# 내 User-Agent와 Accept-language를 입력해야 한국의 한글 페이지에 대한 정보를 가져온다.
headers = {
    "User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36",
    "Accept-language":"ko-KR,ko"
    }

res = requests.get(url, headers=headers)
res.raise_for_status()
soup = BeautifulSoup(res.text, "lxml")

movies = soup.find_all("div", attrs={"class":"ImZGtf mpg5gc"})
print(len(movies))

# 문서 잘 가져오는지 확인
# with open("movie.html", "w", encoding="utf8") as f:
#     f.write(soup.prettify())  # res.text말고 soup.prettify를 쓰면 문서를 예쁘게 가져옴
# 왼쪽에 만들어진 html파일에 우클릭 - Open in Default Browser로 페이지를 열 수 있다.

# 영화 제목 가져오기
for movie in movies:
    title = movie.find("div", attrs={"class":"WsMG1c nnK0zc"}).get_text()
    print(title)