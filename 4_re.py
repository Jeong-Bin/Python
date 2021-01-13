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
        print(m.group())  # group은 일치하는 문자열 반환
        print(m.string) # string은 입력받은 문자열 반환, 괄호 안 씀
        print(m.start()) # start 일치하는 문자열의 시작 index
        print(m.end()) # end 일피하는 문자열의 끝 index
        print(m.span()) # span 일치하는 문자열의 시작과 끝
    else:
        print("매칭되지 않음")

m = p.match("careless")  # 이 경우 매치가 됨. match가 주어진 문자열의 처음부터 일치하는지 확인하기 때문
print_match(m)

m = p.search("good care") # serch는 주어진 문자열 중에 일치하는게 잇는지 확인함.
print_match(m)

lst = p.findall("careless") # 일치하는 모든 것을 리스트 형태로 반환
print(lst)  # 딱 일치하는 부분만 반환됨


# 순서정리
# 1. p = re.compile("원하는 형태")
# 2. m = p.match("비교할 문자열") : 주어진 문자열의 처음부터 일치하는지 확인
# 3. m = p.search("비교할 문자열") : 주어진 문자열 중에 일치하는게 있는지 확인
# 4. lst = p.findall("비교할 문자열") : 일치하는 모든 것을 "리스트" 형태로 반환

# 원하는 형태 : 정규식
# . : 하나의 문자를 의미 (예, ca.e) -> care, cafe, case
# ^ : 문자열의 시작 (예, ^de) -> desk, destination
# $ : 문자열의 끝 (예, se$) -> case, base
