import RPi.GPIO as GPIO
import time

LED_PIN = 18
GPIO.setmode(GPIO.BCM)
GPIO.setup(LED_PIN, GPIO.OUT)

try :
    while True:
        num = int(input('1) LED ON 2) LED OFF 0) QUIT : '))
        if num == 1:
            GPIO.output(LED_PIN, GPIO.HIGH)
            print('LED ON')
        elif num == 2:
            GPIO.output(LED_PIN, GPIO.LOW)
            print('LED OFF')
        elif num == 0:
            GPIO.cleanup()
            print("Exit program")
            break
        else:
            print("0~2 사이의 값을 입력하세요.")
except KeyboardInterrupt:
    print("프로그램 강제 종료")
finally:
    GPIO.cleanup()
