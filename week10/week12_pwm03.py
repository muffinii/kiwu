# PWM은 GPIO 12, 13, 18번 이용 가능
from gpiozero import PWMLED
from time import sleep

led1 = PWMLED(12)
led2 = PWMLED(13)

try :
    while True:
        for value in range(0, 101): # 0, 1, 2 ..., 100 로 duty cycle을 증가
            led1.value = value / 100
            led2.value = 1 - (value / 100)
            sleep(0.02) # 0.02sec
        for value in range(100, -1, -1): # 100, 99, 98 ... 0 로 duty cycle을 감소
            led1.value = value / 100
            led2.value = 1 - (value / 100)
            sleep(0.02) # 0.02sec
except KeyboardInterrupt:
    print("Exit program!")
finally:
    led1.close()
    led2.close()