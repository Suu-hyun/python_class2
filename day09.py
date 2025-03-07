# 사용자 정의 함수
# 사용자가 직접 만들어 사용하는 함수
# 매개변수와 return
# 함수를 호출할 때 전달되는 값을 저장하는 변수
# 함수 내에서 계산한 결과를 함수 외부로 반환
# ============================================================
# 사용자 정의 함수

# 기본적인 사용자 정의 함수
# def func1():
#     print("hello World")
#
# func1()

# def plus():
#     a = 2
#     b = 3
#     print(a + b)
#
# plus()

# 매개변수가 있는 사용자 정의 함수
# def hello(name):
#     print(f"안녕하세요 저는 {name} 입니다.")
#
# hello("이동윤")
# hello(123) # 괄호 안에 매개변수를 입력해야한다.

# def plus(x, y):
#     print(x + y)
#
# plus(5, 6)

# def hello(name = "홍길동"):
#     print(f"안녕하세요 {name}입니다.") # 기본값을 미리 지정이 가능하다.
#
# hello()
# hello("이동윤")

# def introduce(name, age):
#     print(f"제 이름은 {name}이고 나이는 {age}입니다.")
#
# introduce(age = 27, name = "이동윤") # 매개변수는 항상 순서를 지켜줘야함, 단 지정이 가능함.

#리턴 값이 있는 사용자 정의 함수

# def plus(x, y):
#     return x + y
#
# result = plus(1,2)
# print(result)
# print(plus(1, 2))

# def multiple_seven(num):
#     return num * 7
#
# print(multiple_seven(3))
# print(multiple_seven(100))

# def check_divide_seven(num):
#     if num % 7 == 0:
#         return True
#     else:
#         return False
#
# print(check_divide_seven(14))
# print(check_divide_seven(15))

# def factorial(num):
#     sum = 1
#
#     for n in range(num):
#         print(f"n = {n}")
#         sum = sum * (n + 1)
#         print(f"sum = {sum}")
#
#     return sum
#
# print(factorial(7))

# def cal_average(scores):
#
#     sum = 0
#
#     for score in scores:
#         sum += score
#
#     return sum / len(scores)
#
# score_list1 = [55, 70, 100]
# score_list2 = [100, 99, 88]
# score_list3 = [80, 70, 60]
#
# print(cal_average(score_list1))
# print(cal_average(score_list2))
# print(cal_average(score_list3))

# 콜백함수
# 함수를 매개변수로 전달하여 필요할 때 호출하도록 하는 개념
# 어떤 함수가 실행되는 동안 미리 정의된 다른 함수를 호출하여 실행하는 역활

# def calculator(x, y, operation):
#     return operation(x, y)

# def plus(x, y):
#     return x + y

# def minus(x, y):
#     return x - y

# def multitiple(x, y):
#     return x * y

# def divide(x, y):
#     return x / y

# print(calculator(4, 8, plus)) # 함수명만 적어줘야함 ()안에 적지 않음.
# print(calculator(8, 4, minus))
# print(calculator(8, 4, multitiple))
# print(calculator(8, 4, divide))

# import time
#
# def timer(pause_second, callback):
#     print(f"{pause_second}초 타이머가 시작되었습니다.")
#     print(f"{pause_second}초 뒤에 함수가 실행됩니다.")
#
#     time.sleep(pause_second)
#
#     callback()
#     print("타이머가 종료되었습니다.")
#
# def hello():
#     print("안녕")
#
# timer(5, hello)

# lambda 함수(익명함수, 미시함수)
# 특정 범위 내에서만 사용되거나 호출되는 횟수가 한 번인 경우에 매우 유용
# lambda 매개변수1, 매개변수2, ...: 함수 내부 코드

# def plus(x, y):
#     return x + y

# print(plus(4, 5))

# add_lambda = lambda x, y: x + y
# print(add_lambda(4, 5))

# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# double = list(map(lambda x: x * 2, numbers)) # lambda 함수, map을 씀
# print(double)

# parity = lambda x: "짝수" if x % 2 == 0 else "홀수"

# print(parity(2))


#1. 두 수를 입력받고 두 수의 합을 출력하는 함수
# 내가만든 답
# def sum():
#     x = int(input("x: "))
#     y = int(input("y: "))
#     print(x + y)

# sum()
# 선생님 답
# a = int(input("첫번째 숫자: "))
# b = int(input("두번째 숫자: "))
#
# def add_func (x,y):
#     print(x + y)
#
# add_func(a, b)

#2. 숫자 하나를 입력 받고 해당 숫자가 짝수이면 짝수를 출력하고 홀수이면 홀수를 출력하는 함수
# x = int(input("숫자를 입력하시오.: "))
#
# def a(num):
#     if num % 2 == 0:
#         print("짝수입니다.")
#     else:
#         print("홀수입니다.")
# a(x)

#선생님 답
# a = int(input("숫자: "))
#
# def parity(x):
#     if x % 2 == 0:
#         print("짝수")
#     else:
#         print("홀수")

# parity(a)