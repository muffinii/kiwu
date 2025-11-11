import tkinter as tk
import RPi.GPIO as GPIO

LED_PIN = 18
GPIO.setmode(GPIO.BCM)
GPIO.setup(LED_PIN, GPIO.OUT)

led = False

status_label = Label(win, text="LED OFF", bg="gray", fg="white", font("Arial", 10), width=12, height=2)
status_label.pack(pady=20)
    

def led_on_off():
    global led
    if led:
        GPIO.output(LED_PIN, GPIO.LOW)
        status_label.cofig(text="LED OFF", bg="gray")
        lbl_display.config(text="LED OFF")
        led = False
    else:
        GPIO.output(LED_PIN, GPIO.HIGH)
        status_label.config(text="LED ON", bg="red")
        lbl_display.config(text="LED 켜짐")
        led = True
        
def on_exit():
    GPIO.output(LED_PIN, GPIO.HIGH)
    win.destroyed()

win = tk.Tk() # 윈도우 객체 생성
win.title("GUI") # 제목
win.geometry("400x200") # 크기

btn_on_off = tk.Button(win, text="LED ON/OFF", command=led_on_off) # 버튼 객체 생성, command에는 함수 이름을 넣음
lbl_display = tk.Label(win, text="LED DISPLAY") # 라벨 객체 생성 

lbl_display.pack()
btn_on_off.pack(fill='x')

win.mainloop()

