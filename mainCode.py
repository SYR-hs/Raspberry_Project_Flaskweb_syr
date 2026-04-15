from flask import Flask, request, render_template          # 웹 서버 만드는 Flask 라이브러리
from gpiozero import LED                                   # 라즈베리 파이 GPIO 핀 제어 라이브러리

app = Flask(__name__)                                      # Flask 앱 생성

red_led = LED(21)                                          # 21번 핀에 연결된 LED 설정

@app.route('/')                                            # 기본 주소(/) 접속 시 실행
def home():
   return render_template("index.html")                    # index.html 파일을 브라우저에 보여

@app.route('/data', methods = ['POST'])
def data():
    data = request.form['led']
    
    if(data == 'on'):
        red_led.on() 
        return home()

    elif(data == 'off'):
        red_led.off() 
        return home()

if __name__ == '__main__':
   app.run(host = '0.0.0.0', port = '80')
