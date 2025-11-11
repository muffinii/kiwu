import RPi.GPIO as GPIO
import time

LED_PIN = 18 # BOARD 18
GPIO.setmode(GPIO.BCM) # BCM 모드로 만듦
GPIO.setup(LED_PIN, GPIO.OUT) # set output (출력핀 설정)

# ctrl + c를 입력하면 프로그램이 종료되게 함
try :
    while True:
        GPIO.output(LED_PIN, GPIO.HIGH) # HIGH : 전압을 보냄 / GPIO.HIGH 대신 1을 써도 됨
        time.sleep(2) # delay 2sec
        GPIO.output(LED_PIN, GPIO.LOW) # HIGH : 전압을 보냄 / GPIO.LOW 대신 0을 써도 됨
        time.sleep(2) # delay 2sec
except KeyboardInterrupt:
    print("Exit program")
finally:
    GPIO.cleanup() # GPIO 설정 초기화