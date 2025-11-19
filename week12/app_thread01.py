import time
import threading

print("=== 스레드로 실행 ===")
def count_task(name, count) :
    for i in range(count):
        print(f"{name} :{i + 1}")
        time.sleep(0.5) # 0.5초

start = time.time()

t1 = threading.Thread(target=count_task, args=("작업A", 3)) #target은 함수 이름을 지정해줌, args를 통해 함수에 인수를 전달
t2 = threading.Thread(target=count_task, args=("작업B", 3))

t1.start()
t2.start()

t1.join() # 이 작업이 끝나야 다음으로 넘어감(쓰지 않으면 총 소요시간이 먼저 출력됨)
t2.join()

print(f"총 소요시간: {time.time() - start:.1f}초\n")