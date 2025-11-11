from gpiozero import LED

led = LED(5)

try :
    while True:
        num = input('1) LED ON 2) LED OFF 0) QUIT : ')
        if num == "1":
            led.on()
            print('LED ON')
        elif num == "2":
            led.off()
            print('LED OFF')
        elif num == "0":
            print("프로그램을 종료합니다")
            break
        else:
            print("0~2 사이의 값을 입력해 주세요.")
except KeyboardInterrupt:
    print("Exit program")
except Exception as e:
    print(f"에러 발생: {e}")
finally:
    led.close()
