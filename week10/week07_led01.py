import RPi.GPIO as GPIO
import time

LED_PIN = 17 # BOARD 17
GPIO.setmode(GPIO.BCM) # BCM 모드로 만듦
GPIO.setup(LED_PIN, GPIO.OUT) # set output (출력핀 설정)

while True:
    GPIO.output(LED_PIN, GPIO.HIGH) # HIGH : 전압을 보냄 / LOW : 연결을 끊음
    time.sleep(2) # delay 2sec
    GPIO.output(LED_PIN, GPIO.LOW) # HIGH : 전압을 보냄 / LOW : 연결을 끊음
    time.sleep(2) # delay 2sec
    
GPIO.cleanup() # GPIO 설정 초기화