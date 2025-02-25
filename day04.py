# 딕셔너리(Dictionary)
# 키-값 쌍으로 데이터를 저장하는 자료형
# 키는 고유해야 하며, 키는 사용해서 빠르게 접근가능
# 중괄호{}를 둘러싸여 있음, 각 키와 값은 콜론 : 으로 구분, 쌍은 쉼표, 로 구분
# 키는 문자열과 정수열 사용가능 key-value

#profile = {
#     "name"  : "이동윤",
#     "age"   : 27,
#     "hobby" : ["여행하기", "음악듣기"]
# }

#profile["age"] = 28 # 키가 존재하는것은 수정된다.
#print(profile)

#profile["job"] = "강사"
#print(profile)

#del profile["job"] #삭제
#print(profile)

# profile.keys() # 키만 뽑아내기
#key_list = list(profile.keys())
#key_list.append("job")
#print(key_list)

#profile.values() # 값만 뽑아내기
#value_list = list(profile.values())
#print(value_list)

#profile.items() # 키-갑 형태로 다 뽑아내기
#item_list = list(profile.items())
#print(profile.items())

# item_list = list(profile.items())
# item_list.append(("job", "강사"))
# print(item_list)

# python_grade = {
#     "동윤" : "B",
#     "길동" : "C",
#     "준식" : "A",
#     "상혁" : "D"
# }

#print(sorted(python_grade.items())) #키 기준 오름차순
#print(sorted(python_grade.items(),reverse=True)) # 키 기준 내림차순

#print(sorted(python_grade.items(), key=lambda x: x[1])) #abcd값의 인덱스 번호가 [1], 값 기준으로 오름차순
#print(sorted(python_grade.items(), key=lambda x: x[1],reverse=True)) # reverse=True 옵션을 주면 내림차순

# student = {}
# 이름 입력 받고 점수도 입력 받고 딕셔너리에 저장
#{"name" : "이동윤", "score" : 80}
# 첫번째 방법
# student = {
#     "name": input("이름: "),
#     "score": input("점수: ")
# }
# print(student)

# 두번째 방법
# student["name"] = input("이름: ")
# student["score"] = int(input("점수 : "))
# print(student)

# 세트(Set)
# 중복을 허용하지 않고, 순서가 없는 데이터 모음
# 수학에서 말하는 집합 개념과 유사함

#fruits = {"사과", "바나나", "귤", "귤"} # =>세트
# print(fruits)
# apple_str = set("apple")
# print(apple_str)

#num = {1, 2, 5, 5, 6}
#num.add(8) #추가
#num.remove(19) #삭제(없으면 오류냄)
#num.discard(19) #삭제(없으면 오류안 냄)
#num.update([10, 11, 12])
#print(num)

#empty_set = set() # 빈 세트를 선언
#empty_set = {} # 빈 딕셔너리 선언하는것

#num.clear() # 요소 전체 제거
#print(num)

# a = {1, 2, 3, 4, 5}
# b = {4, 5, 6, 7, 8}

#합집합
# print(a.union(b))
# print(a|b) #shift + \하면 |

#교집합
# print(a.intersection(b)) #intersection은 교집합이라는 뜻
# print(a & b) #shift + 7 치면 &(and)가 나옴

#차집합
# print(a.difference(b)) #a에서 b를 뺀것
# print(a - b)

# color = {"b", "l", "u", "e"}
# print(color.pop()) # 세트는 순서가 지정이 안되기 때문에 랜덤으로 하나가 지워진다.
# print(color)

# a = {21, 22, 23, 25, 26}
# b = {22, 24, 27}
# common = set(a) & set(b)
# print(common)

#문제2
python_class = ["수현", "현호", "지니", "가인"] #리스트이기 때문에 set로 변환
Java_class = ["현호", "지니", "홍수", "찬호"]

#공통으로 출석한 학생:
common_class= set(python_class) & set(Java_class)
print(common_class)
#파이썬만 출석한 학생:
python = set(python_class) - set(Java_class)
print(python)
#자바만 출석한 학생:
Java= set(Java_class) - set(python_class)
print(Java)

