import tkinter as tk

def btn_click(value):
    current_value = entry.get()
    entry.delete(0, tk.END)
    entry.insert(tk.END, current_value + str(value))

def clear():
    entry.delete(0,tk.END)

def equal_sign():
    result = eval(str(entry.get()))
    entry.delete(0, tk.END)
    entry.insert(0, str(result))

root = tk.Tk()
root.title("계산기")
# root.gealid character in identometry("300x300")

entry = tk.Entry(root)
entry.grid(row=0, column=0, columnspan=4)
btn_list = [(7,1,0),(8,1,1),(9,1,2),("/",1,3),(4,2,0),(5,2,1),(6,2,2),("÷",2,3),(1,3,0),(2,3,1),(3,3,2),("×",3,3),(".",4,0),(0,4,1),("＋",4,2)]

for(text,row,col) in btn_list:
    tk.Button(root, text=text, command=lambda t=text:btn_click(t)).grid(row=row, column=col)

tk.Button(root, text="=", command=equal_sign).grid(row=4, column=3)

tk.Button(root, text="clear", command=clear).grid(row=5, column=1, columnspan=2)

root.mainloop()