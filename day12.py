import math

# math - 수학 관련 모듈

# ceil - 올림
# print(math.ceil(3.14))

# copysign - 두 번째 인자의 부호만 취해 첫 번째 인자에 적용
# print(math.copysign(3.14, -1))

# fabs - 절댓값을 반환하는 메소드
# print(math.fabs(-3.14))

# factorial - 팩토리얼 구하는 메소드
# print(math.factorial(7))

# floor - 내림
# print(math.floor(3.14))

# gcd - 두 수의 최대공약수
# print(math.gcd(6, 8))

# modf - 정수 부분과 소수 부분을 분리해서 리턴
# print(math.modf(3.14))

# trunc - 내림
# print(math.floor(-3.14)) # 무조건 아래로 내림
# print(math.trunc(-3.14)) # 0으로 향하는 내림

# log(a, b) - b를 밑으로 하는 log a에 대한 로그 값
# print(math.log(10,10))

# 원주율
# print(math.pi)

import random # random 모듈

# 난수
# print(random.random()) # 실수
#
# print(random.randint(1,10)) # 1부터 10까지/ 무작위 숫자 정수로 나오게 해주는 randint
#
# print(random.randrange(1,10, 2)) # randint와 같지만 randint는 스텝 설정이 없다.

# suffle
# abc = ["a", "b", "c", "d", "e"]
# random.shuffle(abc)
# print(abc)

# choice
# abc = ["a", "b", "c", "d", "e"]
# print(random.choice(abc)) # 리스트 안에 문자 하나를 꺼네줌/ 꼭 리스트 형식일 필요는 없음
#
# menu = "삼겹살", "된장찌개", "맥주", "소주"
# print(random.choice(menu))

from datetime import datetime, timedelta

# 현재 날짜
# now = datetime.now()
# print(now)
#
# one_week_later = now + timedelta(days=7)
# print(one_week_later)
#
# formatted_date = now.strftime("%Y-%m-%d %H:%M:%S") # 형식을 바꿀 수 있다. 소대문자 차이는 month인지 minute인지 구분하기 위함이다.
# print(formatted_date)

import os

# print(os.getcwd()) # 현재 디렉토리
# print(os.listdir()) # 현재 폴더의 파일 목록
#
# if not os.path.exists("new_folder"): # new_folder가 존재하지 않는 다면 새로운 폴더를 만든다
#     os.mkdir("new_folder")

import re

# 정규 표현식은 구글에 쳐서 확인해볼것(식이 다 있음)(올바른 이메일 주소확인)
#-------------표준 묘듈은 여기까지--------------

