import RPi.GPIO as GPIO
import time

# 버튼을 누를 때마다 밝기가 증가, 누르지 않으면 밝기 감소

LED_PIN = 18
BUTTON_PIN = 17
GPIO.setmode(GPIO.BCM)
GPIO.setup(LED_PIN, GPIO.OUT)
GPIO.setup(BUTTON_PIN, GPIO.IN, pull_up_down=GPIO.PUD_UP)

pwm = GPIO.PWM(LED_PIN, 1000)
pwm.start(0)

try:
    dc = 0
    while True:
        state = GPIO.input(BUTTON_PIN)
        if state == 0 and (dc+5) <= 100:
            print("스위치를 눌렀습니다.")
            dc += 5
            pwm.ChangeDutyCycle(dc)
            print(f"현재 밝기 : {dc}")
        elif state == 1 and (dc-5) >= 0:
            print("스위치를 누르지 않았습니다.")
            dc -= 5
            pwm.ChangeDutyCycle(dc)
            print(f"현재 밝기 : {dc}")
        elif (dc+5) > 100:
            print("최대 밝기에 도달했습니다.")
        else:
            print("최소 밝기에 도달했습니다.")
        time.sleep(0.5)
except KeyboardInterrupt:
    print("프로그램 종료")
finally:
    GPIO.cleanup()