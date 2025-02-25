# print("Hello World")
#
# name = "이동윤"
# age = 27.15
# "제 이름은 ____ 입니다."
# print("제 이름은" + name + "입니다.") #띄어쓰기 x
# print("제 이름은", name, "입니다") #띄어쓰기 0
#
# "제 나이는 __ 입니다."
# #print("제 나이는" + age + "입니다.") int+str은 불가, 오류발생
# print("제 나이는", age, "입니다.") #쉼표는 변수가 있는 공간
# print("제 나이는 {} 입니다.".format(age)) #format은 {}사이에 들어갈 단어라고 표시
# print("제 나이는 {} 이고 이름은 {} 입니다.".format(age, name)) # args는 힌트
# print("제 나이는 {a} 이고 이름은 {b} 입니다.".format(a=27, b="이동윤")) #문자열 내에서 변수를 만들어 적는게 가능하다.
# print(f"제 나이는 {age} 이고 이름은 {name} 입니다.") #f를 쓰면 {}칸에 변수명을 바로 들어갈 수 있게 만들어준다. (f-string 방식이라 명칭)
# # print("제 이름은 %s 입니다." % age) # s는 str임, int를 str로 바꿔줌.
# print("제 나이는 %s 입니다." % age) # 문자열로 들어간다.
# print("제 나이는 %d 입니다." % age) # %d는 실수를 정수로 바꿔줌, str은 들어갈 수 없음, 모든 숫자가 정수로 들어간다.
# print(f"제 나이는 %d 이고 이름은 %s 입니다." %(age, name)) # f-string방식도 가능
# print("제 지분은 %d%%입니다." % 2) # %%는 %자체로 출력
# # print("%s의 %s점수는 %d점입니다" %("철수", "수학", 20))
#
# print("%0.4f" %3.14156512345) #0.4는 소수점 4번째까지 출력하겠다는 의미 5를 입력하면 5번째까지
# print("%10.2f" %3.14156512345) #공백 6자리, ______3.14=10자리, %"자릿수","몇번째소수점"f
# # 자릿수를 10자리, 수소점은 2번째까지만 출력하겠다라는 의미


# 입력
# input() #함수
# email = input("이메일 : ") #email이라는 변수에 밑에 쓴 것을 넣겠다라는 의미
# hobby = input("취미 : ")
# # address = input("주소 : ")
# age = int(float(input("나이 : "))) #두 번 형변환, 나이가 27.15일때
# # print("제 이메일은 %s이고 취미는 %s이며 주소는 %s입니다." %(email, hobby, address))
# print(f"제 이메일은{email}, 제 취미는 {hobby}, 나이는 {age}")

# 인덱싱은 0으로 시작한다. 역순으로는 -1부터

# a = "Life is too short, You need Python"
# print(a[-1])
#
# # 문자열[start:end:step] 1(start)부터 8(end)까지 2칸(step)씩 띄어서 나타내겠다.
# print(a[4:8]) #8(end)는 자기 앞에 번호까지만 사실상 7까지임
# print(a[:8])
# print(a[4:])
# print(a[2:10:2])

# date = "20250218sunny"
# date2 = "20260505cloudy"
#
# #연도, 월, 일, 날씨
# #연도는 2025, 월은 02 일은 18 날씨는 sunny
#
# print(f"연도는 {date[:4]}, 월은 {date[4:6]}, 일은 {date[6:8]}, 날씨는 {date[8:]}")
# print(f"연도는 {date[:-9]}, 월은 {date[-9:-7]}, 일은 {date[-7:-5]}, 날씨는 {date[-5:]}")
# print(f"연도는 {date[:4]}, 월은 {date[4:6]}, 일은 {date[-7:-5]}, 날씨는 {date[-5:]}")
#
# #선생님 답
# print(f"연도는 {date[:4]}, 월은 {date[4:6]}, 일은 {date[6:8]}, 날씨는 {date[8:]}")

#다양한 문자열 함수 strip는 공백을 지워준다

a = "Life is too short, You need Python"
# print(len(a)) #문자열 길이
# print(a.count("t",5,10)) #문자가 몇개 있는지
# # print(a.index("x")) # 앞에서 부터 찾는데 해당 문자의 인덱스 번호
# # index는 없으면 오류를 낸다
# print(a.find("x")) # 문자열에만 사용 가능
# # find는 없으면 -1을 출력한다.
# print(a.lower()) #upper 소문자/대문자 변환
# print(a[0].isupper()) #true/false
# print(a.replace(""," ")) #원문에 영향을 주진 않는다. 공백을 입력해 띄어쓰기를 제거 가능하다.
# print(a)
# print(a.strip()) # lstrip은 왼쪽 공백제거, rstrip은 오른쪽 공백 제거
# print(a.split())
#
# b = "a:b:c:d"
# print(b.split(":"))

# email = input("email: ") #dongyoon7212@naver.com
# address = input("address: ")
# #id는 dongyoon7212