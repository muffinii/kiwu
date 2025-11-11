import tkinter as tk
import RPi.GPIO as GPIO

def get_input_value():
    num = int(en_input.get())
    if num >= 0 and num <=100:
        pwm.ChangeDutyCycle(num)
        lbl_display.config(text=f'밝기 : {num}')
    else:
        lbl_display.config(text='0에서 100 사이의 값을 입력하세요')
        
LED_PIN = 18
GPIO.setmode(GPIO.BCM)
GPIO.setup(LED_PIN, GPIO.OUT)

pwm = GPIO.PWM(LED_PIN, 1000)
pwm.start(0)

win = tk.Tk() # 윈도우 객체 생성
win.title("GUI") # 제목
win.geometry("400x200") # 크기

en_input = tk.Entry(win, width=15)
btn_click = tk.Button(win, text='Click', width=15, command=get_input_value)
lbl_display = tk.Label(win, text='Display', width=30)

# layout (grid: 행렬)
lbl_display.grid(row=0, column=0, columnspan=2)
en_input.grid(row=1, column=0)
btn_click.grid(row=1, column=1)

win.mainloop()



