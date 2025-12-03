from flask import Flask, render_template, jsonify, request
import RPi.GPIO as GPIO
import time
import threading

app = Flask(__name__)

# GPIO 핀 번호 설정
TRIG = 23
ECHO = 24
LED_PIN = 17

# GPIO 초기화
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(TRIG, GPIO.OUT)
GPIO.setup(ECHO, GPIO.IN)
GPIO.setup(LED_PIN, GPIO.OUT)

# 전역 변수
current_distance = 0
led_status = False

def measure_distance(): # 거리 측정하는 함수
    GPIO.output(TRIG, True) # 1/10초 동안 전파 발사
    time.sleep(0.00001) # 1/10만 초
    GPIO.output(TRIG, False) # 전압을 다시 0V로
    
    start_time = time.time()
    timeout = time.time() + 0.1  # 100ms 타임아웃
    
    while GPIO.input(ECHO) == 0 and time.time() < timeout:
        start_time = time.time()
    
    while GPIO.input(ECHO) == 1 and time.time() < timeout:
        end_time = time.time()
    
    try:
        elapsed_time = end_time - start_time # 왔다갔다한 시간
        distance = (elapsed_time * 34300) / 2 # 왕복이라서 /2를 해줌
        return round(distance, 2) # 소수점 둘째 자리까지만 표시
    except:
        return -1  # 에러 시

def update_sensor_data():
    global current_distance # 전역변수
    while True:
        current_distance = measure_distance() # 거리를 받아와서 저장
        time.sleep(0.5) # 0.5초간 delay

# 백그라운드에서 센서 데이터 업데이트
sensor_thread = threading.Thread(target=update_sensor_data) # thread 객체 생성, target에 함수 바인딩(binding)
sensor_thread.daemon = True # daemon: 백그라운드 스레드, True: 메인 프로그램이 종료되면 sensor_thread가 끝나지 않았더라도 함께 종료하란 뜻(종속적임)
sensor_thread.start() # 실제 시작

@app.route('/') # 메인에 접속했을 때
def index():
    return render_template('index.html')

@app.route('/get_distance')
def get_distance():
    return jsonify({'distance': current_distance}) # 거리를 json 형태로 넘김?

@app.route('/led/<action>') # 클릭했을 때 동작
def control_led(action):
    global led_status
    if action == 'on':
        GPIO.output(LED_PIN, GPIO.HIGH)
        led_status = True
        return jsonify({'status': 'LED ON'})
    elif action == 'off':
        GPIO.output(LED_PIN, GPIO.LOW)
        led_status = False
        return jsonify({'status': 'LED OFF'})
    return jsonify({'status': 'Invalid action'})

@app.route('/get_led_status')
def get_led_status():
    return jsonify({'led_on': led_status})

if __name__ == '__main__':
    try:
        app.run(host='0.0.0.0', port=5000)
    except KeyboardInterrupt:
        GPIO.cleanup()