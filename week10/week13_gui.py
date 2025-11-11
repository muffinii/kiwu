import tkinter as tk

win = tk.Tk() # 객체 생성
win.title("GUI") # 제목
win.geometry("400x200") # 크기
win.resizable(False, False) # 크기 고정

btn_test = tk.Button(win, text="IoT GUI 실습 중...")
btn_test.pack()

win.mainloop()