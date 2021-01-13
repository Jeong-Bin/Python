# 정규식(특정한 규칙이 있는 주민등록번호, 이메일, 차량번호 등이 정규식임)

import re

# ca?e 라는 단어를 찾으려면?
p = re.compile("ca.e")
# . : 하나의 문자를 의미 (예, ca.e) -> care, cafe, case
# ^ : 문자열의 시작 (예, ^de) -> desk, destination
# $ : 문자열의 끝 (예, se$) -> case, base

# 정규식과 매치가 되는지 확인
m = p.match("case")
print(m.group()) # 매치가 되면 출력

m = p.match("caffe")
print(m.group()) #  매치가 안 되면 에러

# 함수-조건문으로
def print_match(m):

    if m:
        print(m.group())
    else:
        print("매칭되지 않음")

m = p.match("caffe")
print_match(m)
