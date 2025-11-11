# PWM은 GPIO 12, 13, 18번 이용 가능
import RPi.GPIO as GPIO
import time

LED_PIN = 18 # BOARD 12
GPIO.setmode(GPIO.BCM) # BCM 모드로 만듦
GPIO.setup(LED_PIN, GPIO.OUT) # set output (출력핀 설정)

pwm = GPIO.PWM(LED_PIN, 1000) # 두 번째 인수는 주파수 설정, 단위 1kHz = 1000Hz, pwm 객체 생성
pwm.start(0) # Duty cycle을 0%로 할당

try :
    while True:
        for dc in range(0, 101, 5): # 0, 5, 10, ..., 100 로 duty cycle을 증가
            pwm.ChangeDutyCycle(dc)
            time.sleep(0.05) # 0.05sec
        for dc in range(100, -1, -5): # 100, 95, 90, ... 0 로 duty cycle을 감소
            pwm.ChangeDutyCycle(dc)
            time.sleep(0.05) # 0.05sec
except KeyboardInterrupt:
    print("Exit program")
finally:
    pwm.stop()
    GPIO.cleanup() # GPIO 설정 초기화
