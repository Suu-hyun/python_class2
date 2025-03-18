import time
import json

def save_todo(todo_list):
    with open("todo.json", "w", encoding="utf-8") as file:
        json.dump(todo_list, file, indent=4, ensure_ascii= False)

    print("저장되었습니다!")

def add():
    todo_list = []
    while True:
        todo_name = input("할 일을 입력해주세요.(그만하려면 종료) : ")
        todo_complete = False
        if todo_name == "종료":
            save_todo(todo_list)
            break

        todo_list.append({"해야 할 일 : ": todo_name, "완료 여부: ": todo_complete})

def check():
    with open("todo.json", "r", encoding="utf-8") as file:
        todo_list = list(json.load(file))

    for i in range(0,len(todo_list)):
        print(f"{i + 1}. 할 일 : {todo_list[i]["todo_name"]}")
        print(f"완료 상태 : {"완료" if todo_list[i]["todo_complete"] else "미완료"}")

    return todo_list

def update():
    todo_list = check()
    while True:
        choice_todo = int(input("수정하고 싶은 할 일 번호 : "))




while True:
    print("**********메뉴***********")
    print("""
        1. 오늘 할 일 추가
        2. 오늘 할 일 조회
        3. 오늘 할 일 수정
        4. 오늘 할 일 완료
        5. 오늘 할 일 삭제
        6. 종료
    """)

    choice = int(input("메뉴를 선택해주세요. : "))
    if choice == 1:
        add()
    elif choice == 2:
        check()
    elif choice == 3:
        print("오늘 할 일 수정")
    elif choice == 4:
        print("오늘 할 일 완료")
    elif choice == 5:
        print("오늘 할 일 삭제")
    elif choice == 6:
        break
    else:
        print("메뉴를 다시 선택해주세요!!!")
        continue


