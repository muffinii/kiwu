from flask import Flask, render_template, request, redirect, url_for
# import RPi.GPIO as GPIO
from gpiozero import LED

app = Flask(__name__)

# GPIO 설정
# GPIO.setmode(GPIO.BCM)
# LED1 = 20
# LED2 = 21
led1 = LED(20)
led2 = LED(21)

# GPIO.setup(LED1, GPIO.OUT)
# GPIO.setup(LED2, GPIO.OUT)

# LED 상태 저장
led_states = {'led1': 0, 'led2': 0}

@app.route('/')
def index():
    return render_template('index.html', states=led_states)

@app.route('/led/<int:led_num>/<int:state>')
def control_led(led_num, state):
    """개별 LED 제어"""
    if led_num == 1:
        if state == 1: #켜져있는경우
            led1.on()
        else:
            led1.off()
        led_states['led1'] = state
    elif led_num == 2:
        if state == 1:
            led2.on()
        else:
            led2.off()
        led_states['led2'] = state
    
    return redirect(url_for('index'))

@app.route('/all/<int:state>')
def all_leds(state):
    """모든 LED 동시 제어"""
    # GPIO.output(LED1, state)
    # GPIO.output(LED2, state)
    if state == 1:
        led1.on()
        led2.on()
    else:
        led1.off()
        led2.off()
    led_states['led1'] = state
    led_states['led2'] = state
    
    return redirect(url_for('index'))

if __name__ == '__main__':
    try:
        app.run(host='192.168.5.129', port=5000)
    finally:
        # GPIO.cleanup()
        pass