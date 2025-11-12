import RPi.GPIO as GPIO
import time

# led 2개 연결
RED_LED_PIN = 20
GREEN_LED_PIN = 21
GPIO.setmode(GPIO.BCM)
GPIO.setup(RED_LED_PIN, GPIO.OUT)
GPIO.setup(GREEN_LED_PIN, GPIO.OUT)

try :
    while True:
        # 2개를 번갈아가며 키기
        GPIO.output(RED_LED_PIN, GPIO.HIGH)
        GPIO.output(GREEN_LED_PIN, GPIO.LOW)
        time.sleep(2)
        GPIO.output(RED_LED_PIN, GPIO.LOW)
        GPIO.output(GREEN_LED_PIN, GPIO.HIGH)
        time.sleep(2)
except KeyboardInterrupt:
    print("Exit program")
finally:
    GPIO.cleanup()