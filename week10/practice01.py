import RPi.GPIO as GPIO
import time

# 스위치를 누르면 초음파 센서 발사

# GPIO 핀 번호 정의
TRIG = 23
ECHO = 24
BUTTON_PIN = 17
GPIO.setmode(GPIO.BCM)
GPIO.setup(BUTTON_PIN, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(TRIG, GPIO.OUT)
GPIO.setup(ECHO, GPIO.IN)
GPIO.output(TRIG, False)

def get_distance():
    # 초음파 발사
    GPIO.output(TRIG, True)
    time.sleep(0.00001)  # 10us
    GPIO.output(TRIG, False)
    
    # ECHO 핀에 HIGH가 될 때까지 측정
    pulse_start = time.time()
    time_out = pulse_start + 1
    while GPIO.input(ECHO) == 0:
        pulse_start = time.time()
        if pulse_start > time_out:
            return -1
    
    # ECHO 핀에 LOW가 될 때까지 측정
    pulse_end = time.time()
    time_out = pulse_end + 1
    while GPIO.input(ECHO) == 1:
        pulse_end = time.time()
        if pulse_end > time_out:
            return -1
    
    # 시간차 계산
    pulse_duration = pulse_end - pulse_start
    # 거리 계산 (음속 34300cm/s)
    distance = pulse_duration * 34300 / 2
    return round(distance, 2)


try:
    while True:
        state = GPIO.input(BUTTON_PIN)
        print(f"스위치 상태 : {state}")
        if state == 0:
            distance = get_distance()
            if distance == -1:
                print("측정 오류: 신호를 받지 못함")
            else:
                print(f"거리: {distance}cm")
            time.sleep(0.5)
        time.sleep(0.3)
except KeyboardInterrupt:
    print("프로그램 종료")
finally:
    GPIO.cleanup()