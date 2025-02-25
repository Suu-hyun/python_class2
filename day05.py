# x= 10
# x += 10 # 더하고 대입(할당) x = x +10
# x -= 5 # 빼고 대입(할당) x = x - 5
# x *= 3 # 곱하고 대입(할당) x = x * 3
# x /= 2 # 나누고(몫이 실수) 대입(할당) x = x / 2 => 값은 5.0
# x//=2 #나누고(몫이 정수) 대입(할당) x = x // 2 =>값은 5
# print(x)

# x = 10
# y = 20
# z = 10
# print(x == z) # == 같다
# print(x != z) # != 다르다
# print(x > y) # 왼쪽기준 오른쪽보다 크다
# print(x > z) # 같기때문에 false
# print(x < y) # 왼쪽기준 오른쪽보다 작다
# print(x >= z) # 크거나 같다
# print(x <= y) # 작거나 같다

# or에서 false or false일때 false가 출력된다.
# a = True
# b = False
# print(a and b)
# print(a or (a and b))
# print(not a)
# print(not a and b)

# 조건연산자 (삼항연산자)
# a = 10
# b = 20
# max_value = a if a > b else b # a와 b중에 무엇이 더 큰지, a>b가 true면 a fasle면 b
# print(max_value)

# score = 85
# grade = "A" if score>=90 else ("B" if score >= 80 else "C")
# print(grade)
# 90점 이상일 때 a 80점 이상일 때 b 70점 이상일 때 c

# if a > b:
#     max_value = a
# else:
#     max_value = b
# score = 85
# elif 조건을 쓰고 조건이 하나 더 있다는 뜻 else if
# if score >= 90:
#     print("A")
# elif score >= 80:
#     print("B")
# else:
#     print("C")


