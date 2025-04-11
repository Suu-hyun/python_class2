import tkinter as tk
from tkinter import messagebox

# 기본 창 구성
# root = tk.Tk() # 창 생성
# root.title("GUI프로그래밍 실습") # 창 제목(타이틀)
# root.geometry("800x800") # 창 크기 설정(가로x세로)
# root.resizable(False, False) # 창 크기 조절 가능(True)/불가능(False)
#
# label = tk.Label(root, text="안녕하세요", fg="red", bg="blue") # 텍스트 또는 이미지
# label.pack(side="left") # top, bottom, left, right
#
# def button_click():
#     print("클릭됨")
#     print(chk_var.get())
#     print(radio_var.get())
#     root.quit() # 종료
#
# button = tk.Button(root, text="종료", command=button_click)
# button.pack(side="bottom")
#
# entry = tk.Entry(root)
# entry.pack(side="top")
#
# text = tk.Text(root, wrap= "word") # wrap => 줄바꿈 타입
# # none : 줄 내림 하지 않음
# # cahr : 글자 단위로 줄 내림
# # word : 단어 단위로 줄 내림
# text.pack(side="top")
#
# chk_var = tk.IntVar()
# chk = tk.Checkbutton(root, text="위 내용에 거짓이 없음을 동의합니다.", variable=chk_var)
# chk.pack(side="bottom")
#
# def value_print() :
#     print(radio_var.get())
#
# radio_var = tk.StringVar()
# r1 = tk.Radiobutton(root, text="옵션 1", variable=radio_var, value="옵션 1", command=value_print)
# r2 = tk.Radiobutton(root, text="옵션 2", variable=radio_var, value="옵션 2", command=value_print)
# r3 = tk.Radiobutton(root, text="옵션 3", variable=radio_var, value="옵션 3", command=value_print)
# r1.pack(side="top")
# r2.pack(side="top")
# r3.pack(side="top")



# root.mainloop() # 창 실행

# 레이아웃

# root = tk.Tk()
# root.title("레이아웃 실습")
# root.geometry("800x600")

# label = tk.Label(root, text="안녕하세요")
# label.place(x=0, y=0)

# label2 = tk.Label(root, text="반갑습니다")
# label2.place(x=800, y=0)

# label5 = tk.Label(root, text="qk")
# label5.place(x=0, y=200)

# label3 = tk.Label(root, text="소통해요")
# label3.place(x=0, y=300)

# label4 = tk.Label(root, text="파이썬입니다")
# label4.place(x=0, y=400)


# root.mainloop()
# grid에 rawspan, columnspan이 존재

root = tk.Tk()
root.title("회원가입 창")
root.geometry("500x200")

id_label = tk.Label(root, text="아이디 : ")
id_label.grid(row=0, column=0, pady=10) # x가 row, y가 column

id_entry = tk.Entry(root)
id_entry.grid(row=0, column=1, pady=5)

def dupl_click():
    tk.messagebox.showinfo("중복확인", "중복확인 되었습니다.")

dupl_btn = tk.Button(root, text="중복확인", command=dupl_click)
dupl_btn.grid(row=0, column=2)

password_label = tk.Label(root, text="비밀번호 : ")
password_label.grid(row=1, column=0)

password_entry = tk.Entry(root, show="*")
password_entry.grid(row=1, column=1, pady=5)
chk_vat = tk.IntVar()
chk = tk.Checkbutton(root, text="약관 내용에 동의합니다.", variable=chk_vat)
chk.grid(row=2, column=1)

def signup_click():


    if chk_vat.get() ==0:
        chk_value = "동의 안함"
    else:
        chk_value = "동의 함"
    tk.messagebox.showinfo("회원가입 완료", f"아이디:{id_entry.get()}\n 약관동의:{chk_value}")

signup_btn = tk.Button(root, text="회원가입", command=signup_click)
signup_btn.grid(row=3, column=2)

root.mainloop()

# 끝