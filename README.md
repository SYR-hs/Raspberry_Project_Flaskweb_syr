# Raspberry_Project_Flaskweb_syr

소스코드는 mainCode.py 파일에 정리되어 있습니다.

라즈베리파이 가스감지 시연 영상 링크: 

----

# 추가적으로 찾아본 내용

## render_template("index.html"), request.form['led'] 코드에 대하여

render_template("index.html") : 파이썬과 HTML의 '연결 고리'
플라스크에서 제공하는 함수다.

사용자에게 HTML 파일을 보여줘! 라고 명령하는 역할을 한다.

특징: 이 함수는 약속된 장소인 templates 폴더 안에서 해당 파일을 찾는다. 단순히 파일을 읽어오는 것을 넘어, 앞서 설명한 Jinja2 엔진을 가동시켜 HTML 내부에 심어진 파이썬 코드들을 최종적인 결과물로 완성한 뒤 사용자(브라우저)에게 전송한다.

request.form['led'] : 브라우저가 보낸 '편지 내용 확인'
플라스크의 request 객체 안에 있는 데이터 꾸러미다.

사용자가 브라우저에서 버튼을 눌렀을 때, 그 버튼이 어떤 데이터(예: 'on' 혹은 'off')를 담고 있는지 서버가 알아내기 위해 사용한다.

- request: 브라우저가 보낸 모든 정보(IP 주소, 데이터 방식 등)가 담긴 가방.

- .form: 그중에서 사용자가 입력 폼(Form)을 통해 보낸 데이터들만 모아둔 꾸러미.

- ['led']: 꾸러미 안에서 'led'라는 이름표가 붙은 실제 값을 꺼내라! (HTML 코드의 name="led"와 연결됩니다.)

## Jinja2 에 대하여

플라스크에 내장된 템플릿 엔진(Template Engine)의 이름.

보통 HTML은 정적이라서 한 번 작성하면 내용이 바뀌지 않지만, Jinja2를 사용하면 HTML 코드 안에 파이썬 변수나 제어문(if, for 등)을 심을 수 있다.

파이썬에서 계산된 결과(예: 센서 값, LED 상태)를 웹 화면에 동적으로 보여주기 위해 사용한. 예를 들어 HTML에 {{ state }}라고 적어두면, Jinja2가 이를 파이썬에서 넘겨준 실제 값으로 바꿔치기해 줍니다.
```
from gpiozero import Buzzer, MCP3208
import time

bz = Buzzer(18)
gas = MCP3208(channel=0)

try:
    while 1:
        gasValue = gas.value * 100
        print(gasValue)
        if gasValue >= 10:
            bz.on()
        else:
            bz.off()

        time.sleep(0.2)


except KeyboardInterrupt:
    pass

bz.off()
```

## 두 코드를 통해 활용 방식의 차이 비교

main6-2.py 코드는 가스가 얼마나 있는지 데이터를 수집하고 분석하고 싶을 때 적합하다.

mainCode.py 코드는 가스가 새면 경고 부저만 울리면 되는 간단한 장치를 만들 때 적합하다.
