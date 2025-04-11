# 제어문
"""

조건문
반복문 (for, while)
"""

# 조건문
# num = int(input("숫자를 입력해 주세요"))
# if num > 0:
#     print("양수입니다.")
# else:
#     print("음수입니다.")

# input_str = input("점수를 입력해 주세요")
# if input_str.isdigit():
#     if int(input_str) >= 90:
#         print("A입니다.")
#     elif int(input_str) >= 80:
#         print("B입니다.")
#     elif int(input_str) >= 70:
#         print("C입니다.")
#     else:
#         print("D입니다.")
# else:
#     print("숫자가 아닙니다.")

# 숫자를 입력받고 짝수인지 홀수인지 판별

# num = int(input("숫자를 입력해 주세요: "))
# if num % 2 == 0:
#     print("짝수")
# else:
#     print("홀수")

# 나이랑 학생인지 아닌지 두가지 질문
# 성인이면서 학생이면 성인학생입니다.
# 성인이 아닙니다.
# age = int(input("나이를 입력하세요"))
# student = input("학생입니까?(y/n)")
#
# if age >= 18 and student.lower() == "y": # y가 대문자든 소문자든 소문자로 만들어서 소문자Y가 되어 나온다.
#     print("성인학생 입니다.")
# else:
#     print("성인 학생이 아닙니다.")


# 반복문 while(값이 true일때 계속 반복된다.)
# num = 0
# while num < 10:
#     num += 1 # 조건을 변경할 코드
#     if num % 3 == 0:
#         continue
#
#     print(num)

# 구구단
# dan = 1
# while dan <= 9:
#     n = 1
#     while n <= 9:
#         print(f"{dan}x{n}={dan*n}")
#         n += 1
#     dan += 1

# 5부터 5의 배수를 50이하까지 조건
# 근데 30일때 멈출게요

# num = 5
# while num <= 50:
#     print(num)
#     if num == 30:
#         break
#     num += 5

# 6으로 바꾼것
# num = 6
# while num <= 60:
#     print(num)
#     if num == 30:
#         break
#     num += 6


# 반복문(슬라이싱과 비슷하다) for문

# fruits = ["사과", "바나나", "체리", "딸기"]
# for fruit in fruits:
#     print(fruit)

# 딕셔너리
# score = {
#     "동윤": 80,
#     "종원": 70,
#     "지니": 100
# }
# for key in score:
#
#     print(f"{key}의 점수는 {score[key]}") #키와 값이 있으니 그에따라 접근

# 튜플
# a_tuple = ("안녕", "하세요", "반갑습니다")
# for a in a_tuple:
#     print(a)

#세트
# a_set = {3, 1, 1, 2, 4, 6, 2}
# print(sorted(a_set)) #정렬된 값을 얻을 순 있다.
# for a in sorted(a_set): # 즉석으로 정렬함수를 넣어 줄수있다
#     print(a)

# word = "python"
# for i in word:
#     print(i)

# for i in range(1,10,2): #range(슬라이싱이랑 비슷 사실상 9까지 카운트함)
# for i in range(1, 10):
#     if i == 5: #5는 출력하지않고 올라가서 6부터 시작
#         continue
#     print(i)

# for i in range(2, 101, 2): # 2부터 100까지 짝수로
#     print(i)

#리스트 합 구하기
# total = 0
# num_list = [10, 20, 40, 60, 80]
# for num in num_list:
#     print("num:", num)
#     total += num
#     print("total", total)
#
# print(total) 구구단
# for dan in range(1,10):
#     for n in range(1,10):
#         print(f"{dan}x{n}={dan*n}")