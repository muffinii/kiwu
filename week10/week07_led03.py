from gpiozero import LED
# import time
from time import sleep

led = LED(17) # GPIO PIN 모드로 동작

# ctrl + c를 입력하면 프로그램이 종료되게 함
try :
    while True:
        led.on()
        sleep(2) # delay 2sec
        led.off()
        sleep(2) # delay 2sec
except KeyboardInterrupt:
    print("Exit program")
finally:
    # GPIO.cleanup() # GPIO 설정 초기화, 이 코드에선 GPIO를 사용하지 않아서 아래처럼 사용
    led.close()