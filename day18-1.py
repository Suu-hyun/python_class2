# to_do list(ver.GUI)
import tkinter as tk
from tkinter import messagebox
import json
import os

SAVE_FILE = "save.json" # 상수 변수(변할 일 없는 변수)/ 대문자로 표기하는게 개발자들 사이에서의 국룰 다른걸 써도 상관없음


def add_todo():
    todo = to_do_entry.get()
    if todo:
        to_do_list_box.insert(tk.END, todo) #(어디에?, 무엇을), 'END는 맨 끝에 넣겠다.'라는 뜻
        to_do_entry.delete(0, tk.END)
    else:
        messagebox.showwarning("경고", "할 일을 입력하세요!")

def remove_todo():
    try:
        todo = to_do_list_box.curselection() # 선택된 것들이 튜플 형태로 가져온다.
        if not todo:
            raise IndexError
        to_do_list_box.delete(todo[0])
    except IndexError:
        messagebox.showwarning("경고", "삭제할 할 일을 선택하세요!")

def clear_todo(): # 전체 삭제
    if to_do_list_box.size() == 0: # 리스트의 항목 갯수 => 0개면 아무것도 없는거
        messagebox.showwarning("경고", "삭제할 할 일이 없습니다!")
    else:
        to_do_list_box.delete(0, tk.END)

def save_todo():
    todo_list = to_do_list_box.get(0, tk.END) # 튜플 형태로 다 들고옴
    try:
        with open(SAVE_FILE, "w", encoding="utf-8") as file:
            json.dump(todo_list, file, indent=4, ensure_ascii=False)
        messagebox.showinfo("저장 완료", "저장이 완료되었습니다!")
    except Exception as e:
        messagebox.showerror("오류", f"저장 중 오류 발생:{e}")

def load_todo():
    if os.path.exists(SAVE_FILE):
        try:
            with open(SAVE_FILE, "r", encoding="utf-8") as file:
                todo_list = json.load(file)
                if not isinstance(todo_list, list): # todo_list가 객체 list인지 물어보는 것
                    raise ValueError("올바른 형식이 아닙니다.")
                if to_do_list_box.size() != 0:
                    clear_todo()
                for todo in todo_list:
                    to_do_list_box.insert(tk.END, todo)
        except (json.JSONDecodeError, ValueError):
            messagebox.showerror("오류", "파일 데이터가 손상되었습니다")
        except Exception as e:
            messagebox.showerror("오류", f"불러오기 중 오류 발생:{e}")
        else:
            messagebox.showinfo("불러오기 완료", "불러오기가 완료되었습니다!")
    else:
        messagebox.showwarning("경고", "불러올 저장 파일이 없습니다.")

root = tk.Tk() # 창 생성
root.title("TO DO LIST") # 창 제목(타이틀)
root.geometry("400x500") # 창 크기

to_do_entry = tk.Entry(root, width=40)
to_do_entry.pack(pady=10)

btn_frame = tk.Frame(root)
btn_frame.pack()

add_btn = tk.Button(btn_frame, text="추가", width=10, command=add_todo)
add_btn.grid(row=0, column=0)

remove_btn = tk.Button(btn_frame, text="삭제", width=10, command=remove_todo)
remove_btn.grid(row=0, column=1, padx=10)

clear_btn = tk.Button(btn_frame, text="전체삭제", width=10, command=clear_todo)
clear_btn.grid(row=0, column=2)


to_do_list_box = tk.Listbox(root, width=50, height=20, selectmode="browse")
"""
browse : 하나만 선택(클릭으로) 기본값('selectmode='를 사용하지 않으면 기본값으로 browse가 사용된다.)
single : 하나만 선택(스테이스바)
extended : 여러개 선택(쉬프트나 컨트롤키를 이용해 연속 또는 개별 선택)
multiple : 클릭할 때마다 선택/해제가 가능
"""
to_do_list_box.pack(pady=10)

btn_frame2 = tk.Frame(root)
btn_frame2.pack()

save_btn = tk.Button(btn_frame2, text="저장", command=save_todo)
save_btn.grid(row=0, column=0, padx=20)

load_btn = tk.Button(btn_frame2, text="불러오기", command=load_todo)
load_btn.grid(row=0, column=1, padx=20)

root.mainloop() # 창 실행

# 추가로 할 일 수정도 만들어 볼것
# 끝