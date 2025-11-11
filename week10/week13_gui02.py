import tkinter as tk

def led_on():
    lbl_display.config(text="LED 켜짐")
    
def led_off():
    lbl_display.config(text="LED 꺼짐")

win = tk.Tk() # 윈도우 객체 생성
win.title("GUI") # 제목
win.geometry("400x200") # 크기

btn_on = tk.Button(win, text="LED ON", command=led_on) # 버튼 객체 생성, command에는 함수 이름을 넣음
btn_off = tk.Button(win, text="LED OFF", command=led_off)
lbl_display = tk.Label(win, text="LED DISPLAY") # 라벨 객체 생성 

lbl_display.pack()
btn_on.pack(fill='x')
btn_off.pack(fill='x')

win.mainloop()
