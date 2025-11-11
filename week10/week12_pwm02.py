# PWM은 GPIO 12, 13, 18번 이용 가능
import RPi.GPIO as GPIO
from time import sleep

LED1 = 12
LED2 = 13
GPIO.setmode(GPIO.BCM) # BCM 모드로 만듦
GPIO.setup(LED1, GPIO.OUT) # set output (출력핀 설정)
GPIO.setup(LED2, GPIO.OUT)

pwm1 = GPIO.PWM(LED1, 1000) # 두 번째 인수는 주파수 설정, 단위 1kHz = 1000Hz, pwm 객체 생성
pwm2 = GPIO.PWM(LED2, 1000)
pwm1.start(0) # Duty cycle을 0%로 할당
pwm2.start(0)

try :
    while True:
        for dc in range(0, 101, 1): # 0, 1, 2 ..., 100 로 duty cycle을 증가
            pwm1.ChangeDutyCycle(dc)
            pwm2.ChangeDutyCycle(100 - dc)
            sleep(0.02) # 0.02sec
        for dc in range(100, -1, -1): # 100, 99, 98 ... 0 로 duty cycle을 감소
            pwm1.ChangeDutyCycle(dc)
            pwm2.ChangeDutyCycle(100 - dc)
            sleep(0.02) # 0.02sec
except KeyboardInterrupt:
    print("Exit program")
finally:
    pwm1.stop()
    pwm2.stop()
    GPIO.cleanup() # GPIO 설정 초기화
