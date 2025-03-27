# 에러와 예외
# 에러(Error) : 프로그램 오류 또는 시스템 문제로 발생한 예외(개발자들이 만드는 오류)
# 예외(Exception) : 사용자의 입력 오류에 따라 발생하는 예외
# 예외처리 : 프로그램이 실행될때 발생될 에러를 미리 예측하고 처리해주는 것

# print(10/0) # division by zero이 에로 코드
# num = int(input("숫자를 입력해주세요 : "))
# print(10/num) # ValueError이 에러 이름이고 invalid literal for int() with base 10: 'dkwssud'이 오류내용이다.

# try=except
# try:
#     num = int(input("숫자를 입력해주세요 : "))
#     print(10/num)
# except:
#     print("예외발생!!")

# try-except [발생 예외]
# try:
#     num = int(input("숫자를 입력해주세요 : "))
#     print(10/num)
# except ValueError:
#     print("문자 말고 숫자 넣어라")
# except ZeroDivisionError:
#     print("0말고 딴거 넣어라")

# try:
#     my_list = [1, 2, 3]
#     index = int(input("리스트에서 가져올 인덱스 : "))
#     print(my_list[index])
# except IndexError:
#     print("인덱스 범위가 아닙니다!")
# except ValueError:
#     print("숫자만 입력하쇼")

# try:
#     with open("hi.txt", "r") as file:
#         content = file.read()
# except FileNotFoundError:
#     print("파일 없음")

# try-finally
# try:
#     file = open("hi.txt", "r")
#     content = file.read()
# except FileNotFoundError:
#     print("파일 없음")
# finally:
#     file.close()

# try-except-else
# try:
#     num1 = int(input("숫자1 : "))
#     num2 = int(input("숫자2 : "))
#     result = num1/ num2
# except ValueError:
#     print("숫자만 입력하세요")
# except ZeroDivisionError:
#     print("0이상 숫자를 입력해주세요")
# else:
#     print(result)

# try:
#     file = open("hello.txt", "r")
#     content = file.read()
# except FileNotFoundError:
#     print("파일이 존재하지 않습니다")
# else:
#     print(content)
# finally: # finally는 항상 마지막에
#     file.close()

# 예제 1
# 리스트 요소 5개 선언하고 index 찾는 로직
# 예외처리 하고 정상이면 해당인덱스 값 출력
# 마지막은 항상 "끝!!"을 출력

# 내가 쓴 답
# try:
#     my_list = []
#     for i in range(5):
#         my_list.append(int(input("숫자를 입력하세요 : ")))
#     index = int(input("리스트에서 가져올 인덱스 : "))
#     result = my_list[index]
# except ValueError:
#     print("숫자만 입력하세요")
# except IndexError:
#     print("인덱스 범위가 아닙니다")
# else:
#     print(result)
# finally:
#     print("끝!!")

# 선생님이 쓴 답

# my_list = [1, 2, 3, 4, 5]
# try:
#     index = int(input("인덱스를 입력해주세요"))
#     result = my_list[index]
# except IndexError:
#     print("인덱스 범위 벗어남")
# else:
#     print(result)
# finally:
#     print("끝!!")

# 커스텀 예외 클래스
# try:
#     age = int(input("나이를 입력하세요 : "))
#
#     if age < 0 or age > 150:
#         raise Exception("0이상 150미만 숫자만 입력해주세요")
# except Exception as e:
#     print(e)
# else:
#     print(age)
# finally:
#     print("끝")

# class AgeMyException(Exception):
#     def __init__(self):
#         super().__init__("0이상 150미만 숫자만 입력해주세요")
#
# try:
#     age = int(input("나이를 입력하세요 : "))
#
#     if age < 0 or age > 150:
#         raise AgeMyException()
# except AgeMyException as e:
#     print(e)
# else:
#     print(age)
# finally:
#     print("끝")

# class FundsError(Exception):
#     def __init__(self, balance, amount):
#         super().__init__(f"출금 잔액이 부족 현재 잔액:{balance} 출금 금액:{amount}")
#
# class BankAccount:
#     def __init__(self, balance):
#         self.balance = balance
#
#     def withdraw(self, amount):
#         try:
#             if amount > self.balance:
#                 raise FundsError(self.balance, amount)
#         except FundsError as e:
#             print(e)
#         else:
#             self.balance - amount
#             print(f"정상적으로 출금되었습니다. 남은 잔액: {self.balance - amount}")
#
# account = BankAccount(100000)
# account.withdraw(50000)

# 숙제
# my_dict = {1: "사과", 2: "바나나", 3: "딸기", 4: "포도", 5: "수박"}
# 딕셔너리키를 입력받음(숫자로)
# result 변수에 해당 키의 값을 넣음
# 예외처리는 해당 키가 존재하지 않을 때 => 해당 키는 존재하지 않습니다
# 그리고 숫자가 아닌 문자를 넣었을 때 => 숫자를 입력해주세요
# 정상적으로 실행되면 해당 키의 값을 넣어둔 result 출력
# 마지막은 항상 완료를 출력
try:
    my_dict = {1: "사과", 2: "바나나", 3: "딸기", 4: "포도", 5: "수박"}
    dict_key = int(input("숫자를 입력 : "))
except IndexError:
    print("해당 키는 존재하지않습니다.")