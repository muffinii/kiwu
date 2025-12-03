from flask import Flask, render_template, jsonify
from gpiozero import LED, Button
import time
import random
import threading

app = Flask(__name__) #객체, __name__ : 메인 함수가 실행되면 객체가 생성됨(매직메서드)
#Flask 객체를 생성

# GPIO 설정
led = LED(17)
button = Button(27, pull_up=True)

# 레이스컨디션: 여러 스레드가 공유 자원에 동시에 접근하여 값을 수정하려 할 때 발생
# 스레드 안전성을 위한 락 : 레이스 컨디션과 같은 동기화 문제를 해결하기 위해 사용(자바의 synchronized)
state_lock = threading.Lock()

# 게임 상태
game_state = {
    'status': 'ready',  # 상태 종류 : ready, waiting, measuring, result, early_press, timeout
    'reaction_time': 0, # 반응 시간
    'start_time': 0,
    'best_score': None
}

# 타임아웃 타이머
timeout_timer = None

def game_logic():
    """버튼이 눌렸을 때 실행"""
    global timeout_timer
    
    with state_lock: # with를 벗어나면 lock이 반환됨
        if game_state['status'] == 'measuring': #status: 딕셔너리
            # 정상 반응 - 반응 시간 측정
            reaction = (time.time() - game_state['start_time']) * 1000  # ms로 변환
            game_state['reaction_time'] = round(reaction, 2)
            game_state['status'] = 'result'
            led.off()
            
            # 타임아웃 타이머 취소(리셋)
            if timeout_timer:
                timeout_timer.cancel()
            
            # 최고 기록 업데이트
            if game_state['best_score'] is None or reaction < game_state['best_score']:
                game_state['best_score'] = round(reaction, 2)
        
        elif game_state['status'] == 'waiting':
            # 너무 빨리 누름 (얼리 프레스)
            game_state['status'] = 'early_press'
            game_state['reaction_time'] = 0
            led.off()
            
            # 타임아웃 타이머 취소
            if timeout_timer:
                timeout_timer.cancel()

# 버튼 이벤트 연결
button.when_pressed = game_logic # 버튼이 눌렸을 때 game_logic 실행

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/start', methods=['POST'])
def start_game():
    """게임 시작"""
    global timeout_timer #전역변수
    
    with state_lock:
        if game_state['status'] != 'ready':
            return jsonify({'error': '게임이 이미 진행중입니다'}), 400 # json을 전송, 400: 에러코드
        
        game_state['status'] = 'waiting'
        game_state['reaction_time'] = 0
        game_state['start_time'] = 0
    
    def delayed_led():
        global timeout_timer # 전역변수
        
        # 1~4초 사이 랜덤 대기
        delay = random.uniform(1, 4) # uniform :1~4 까지 수가 일양분포(같은 확률)로 발생
        time.sleep(delay)
        
        with state_lock:
            # waiting 상태가 유지되는지 확인 (얼리 프레스로 취소되지 않았는지)
            if game_state['status'] == 'waiting':
                led.on()
                game_state['start_time'] = time.time()
                game_state['status'] = 'measuring'
        
        # 타임아웃 설정 (5초)
        def handle_timeout():
            with state_lock:
                if game_state['status'] == 'measuring':
                    led.off()
                    game_state['status'] = 'timeout'
                    game_state['reaction_time'] = 0
        
        timeout_timer = threading.Timer(5.0, handle_timeout)
        timeout_timer.start()
    
    thread = threading.Thread(target=delayed_led) # delayed_led : 함수
    thread.daemon = True # daemon: 백그라운드에서 계속 돌아가는 스레드(메인 스레드에 종속되어 있음.)
    thread.start()
    
    return jsonify({'message': '준비... LED가 켜지면 버튼을 누르세요!'})

@app.route('/status')
def get_status():
    """현재 상태 반환"""
    with state_lock:
        return jsonify({
            'status': game_state['status'],
            'reaction_time': game_state['reaction_time'],
            'best_score': game_state['best_score']
        })

@app.route('/reset', methods=['POST'])
def reset_game():
    """게임 리셋"""
    global timeout_timer
    
    # 타임아웃 타이머 취소
    if timeout_timer:
        timeout_timer.cancel()
    
    led.off()
    
    with state_lock:
        game_state['status'] = 'ready'
        game_state['reaction_time'] = 0
        game_state['start_time'] = 0
    
    return jsonify({'message': '리셋 완료'})

if __name__ == '__main__':
    try:
        # 재시작 방지 및 프로덕션 모드
        # import os
        # os.environ['WERKZEUG_RUN_MAIN'] = 'true' # 파일 변경을 감지하고 재시작 명령을 내림. 불필요한 중복 실행, 재귀 실행을 방지
        print("반응속도 게임 서버 시작...")
        print("http://0.0.0.0:5000 접속하세요")
        app.run(host='0.0.0.0', port=5000, use_reloader=False) # 웹서버 객체, 0.0.0.0: localhost
    except KeyboardInterrupt: # Ctrl + C : 종료
        print("\n서버를 종료합니다...")
    finally:
        led.off() # led 끄면서 종료
        print("GPIO 정리 완료")