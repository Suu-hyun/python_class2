#문제2(내가만든 답)
# email = input("이메일: ")
# ID = email[:email.find("@")]
# print(ID)

# email = input("이메일: ")
# ID = email.split("@")[0]
# print(ID)
# email = input("email:")
# ID, Domain = email.split("@")
# print(ID)

# 선생님 정답
# email = input("email : ")#dongyoon7212@naver.com
# #id는 dongyoon7212
# email.find("@")# => index번호 @ 없으면 -1출력 -1번째 방법
# email.index("@")#=> @없으면 오류터짐 -2번째 방법
# print(email[:email.find("@")]) #슬라이싱
# print(email.split("@")[0]) #-3번째 방법

# fruits = ["apple", "orange", "banana"]#리스트
# numbers = [6, 3, 1, 5]# 숫자 리스트
# bools = [True, False, True] #불리언 리스트
# mixed_list = ["안녕하세요", 12, True]

# print(fruits[2][1]) #두번 쓰면 banana 속 문자내 인덱스가능 =>a
# print(fruits[-2])
#
# fruits[1] = "cherry"
# print(fruits)
#
# numbers.append("hi") #append는 요소를 추가해준다. 맨끝에만 추가 가능
# print(numbers)
# numbers.insert(1, 2 ) #1은 인덱스번호, 2는 넣고싶은 수(특정자리요소추가)
# print(numbers)
#
# # numbers.pop()
# print(numbers.pop()) #list의 마지막 요소가 리턴된다.
# numbers.remove("hi")
# print(numbers)
#
# del numbers[4]
# print(numbers)

# print(len(mixed_list)) #리스트의 길이

# fruits.sort() #ctrl + space 단축키
# print(fruits) #작은 순으로 정렬
#
# numbers.sort(reverse=True) #sort() 작은순 /옵션 reverse=True 큰순
# print(numbers)
#
# bools.sort() #문자열+숫자형은 분류가 불가
# # sort()에서 ()안에 값은 reverse=False로 디폴트되어있다.
# print(bools)

# numbers.reverse() # reverse()는 정렬하는게 아닌 그냥 순서를 역순으로 바꿈
# print(numbers)

# fruits = "-".join(fruits) #내가 지정한 요소들을 이어붙인것
# print(fruits)

# 문제 1
#내가 만든 답
# cart= []

# item01 = input("items: ")
# item02 = input("items: ")
# item03 = input("items: ")
# items = item01 + item02 + item03
# cart.append(items)
# print(cart)

#선생님이 만든답
# cart.append(input("추가할 상품: "))
# cart.append(input("추가할 상품: "))
# cart.append(input("추가할 상품: "))

# print(cart)

#튜플은 소괄호
colors = ("red", "green", "black", "yellow") #변경 불가능
numbers = (1, 5, 3, 9, 1)
bools = (True, False, True)
mixed_tuple = ("red", 1, True)

#a = ("first", )# 튜플은 요소가 하나일때는 마지막에 쉼표를 찍어줘야한다.

print(colors[1])

# colors[1] = "yellow" #튜플은 변경불가능
print(numbers[0:2]) #슬라이싱 가능
print(numbers.count(1))
print(numbers.index(3)) # index = 특정 값의 인덱스 번호를 찾는것

a, b, c, d = colors #colors의 첫번째 요소가 a, 두번째 요소가 b, 세번째 요소가 c, 4번째 요소는 d
print(d)