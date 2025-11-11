from tkinter import *
import RPi.GPIO as GPIO

# 밝기 up / down 버튼으로 밝기 조절

RED_LED = 12
GREEN_LED = 13
GPIO.setmode(GPIO.BCM)
GPIO.setup(RED_LED, GPIO.OUT)
GPIO.setup(GREEN_LED, GPIO.OUT)

pwm1 = GPIO.PWM(RED_LED, 1000)
pwm2 = GPIO.PWM(GREEN_LED, 1000)
pwm1.start(0)
pwm2.start(0)

# tkinter 윈도우 생성
win = Tk() 
win.title("LED 제어 GUI")
win.geometry("300x550")

# LED 상태를 저장할 변수
red_led_state = 0
green_led_state = 0

# 레이블 생성 (초기 배경: 회색)
red_status_label = Label(win,
        text="RED LED : 0", bg="gray", fg="white", font=("Arial", 18), width=20, height=2)
red_status_label.pack(pady=20)

green_status_label = Label(win,
        text="GREEN LED : 0", bg="gray", fg="white", font=("Arial", 18), width=20, height=2)
green_status_label.pack(pady=20)

def red_up():
    global red_led_state
    if (red_led_state + 5) <= 100:
        red_led_state += 5
        pwm1.ChangeDutyCycle(red_led_state)
        red_status_label.config(text=f"RED LED : {red_led_state}", bg="red")
    else:
        red_status_label.config(text="RED LED : 최대 밝기", bg="red")

def green_up():
    global green_led_state
    if (green_led_state + 5) <= 100:
        green_led_state += 5
        pwm2.ChangeDutyCycle(green_led_state)
        green_status_label.config(text=f"GREEN LED : {green_led_state}", bg="green")
    else:
        green_status_label.config(text="GREEN LED : 최대 밝기", bg="green")
        
def red_down():
    global red_led_state
    if (red_led_state - 5) >= 0:
        red_led_state -= 5
        pwm1.ChangeDutyCycle(red_led_state)
        red_status_label.config(text=f"RED LED : {red_led_state}", bg="red")
    else:
        red_status_label.config(text="RED LED : 최소 밝기", bg="gray")

def green_down():
    global green_led_state
    if (green_led_state - 5) >= 0:
        green_led_state -= 5
        pwm2.ChangeDutyCycle(green_led_state)
        green_status_label.config(text=f"GREEN LED : {green_led_state}", bg="green")
    else:
        green_status_label.config(text="GREEN LED : 최소 밝기", bg="gray")
        

def on_exit():
    GPIO.cleanup()
    win.destroy()

# LED 제어 버튼
red_up_button = Button(win, text="RED LED UP", command=red_up, height=2, width=13)
red_up_button.pack(pady=10)

red_down_button = Button(win, text="RED LED DOWN", command=red_down, height=2, width=13)
red_down_button.pack(pady=10)

green_up_button = Button(win, text="GREEN LED UP", command=green_up, height=2, width=13)
green_up_button.pack(pady=10)

green_down_button = Button(win, text="GREEN LED DOWN", command=green_down, height=2, width=13)
green_down_button.pack(pady=10)

# 종료 버튼
exit_button = Button(win, text="Exit", command=on_exit, height=2, width=10)
exit_button.pack(pady=5)

win.mainloop()
