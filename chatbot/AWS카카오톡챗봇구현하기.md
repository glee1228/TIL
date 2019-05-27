## AWS에서 Python Flask로 카카오톡챗봇 구현하기

AWS에서 Flask를 사용해서 카카오톡 챗봇을 구현하는 방법 링크:

https://m.blog.naver.com/wool613/221290042134



AWS 운영방법 , SSH 접속 링크:

[http://wool.pe.kr/221286931692](http://wool.pe.kr/221286931692)

AWS에서 Python Flask 사용하기 링크 :

[http://wool.pe.kr/221288013479](http://wool.pe.kr/221288013479)



SSH로 AWS 서버에 접속하는 명령어

(아래의 경로부분은 자신의 PC환경에 맞게 변경한다)

```
ssh -i '/Users/donghoon/공부자료/AWS키페어/aws_key.pem' ubuntu@ec2-3-15-103-190.us-east-2.compute.amazonaws.com
```

* AWS ec2를 만들고 인스턴스 를 연결까지 했다면, 꼭 보안그룹에서 TCP 80, 8080, 5000으로 포트를 열어주길 바란다. 

접속후에는 명령어로 필요한 라이브러리를 설치해준다.

서버가 정상적으로 작동하는 것을 확인했다면 배포(로컬에서 꺼져도 AWS 백그라운드에서 알아서 잘 작동하도록)할 수 있도록 돕는 forever라는 패키지를 활용한다. 

이 패키지(forever)는 주로 nodejs에서 많이 사용하지만 비교적 supervisor와 같은 패키지보다 안정적이고 잘 사용만 한다면, 꿀빨 수 있다.



### forever란? 

npm을 사용해서 npm install forever 명령어로 간단히 설치가 가능하다.
*아주 간단한 명령어를 통해서 node.js로 만든 앱을 실행시켜주고 예기치 않게 종료되었을때 다시 실행해주거나*
*stdout을 로그파일로 남겨주는 등의 관리를 해주는 툴입니다.*
*결론적으로, 아직까지는 안정적인 것 같고 관리하고 편합니다.*

* 사용해야 하는 이유 : 로컬 PC에서 AWS로 접속해 python을 실행시키고 있는동안(서버가 작동하는동안)에는 올바르게 웹서버가 작동을 했지만 로컬 PC의 터미널을 끄면 서버도 함께 꺼지는 현상이 발생하여 로컬 PC와 무관하게 AWS인스턴스에서 웹서버가 꺼질경우 자동으로 재시작해주는 툴이 필요함.(배포)

### forever 사용하면서 에러 및 실시간 요청 확인 하는 방법

**설치는 npm 모듈로 npm install 로 가능하다.**

```
$ sudo npm install forever -g
```

**자주 쓰이는 모듈이기 때문에 -g 옵션으로 글로벌 설치를 하면 편리하다.**

 ```
$ forever --help
 ```

### 명령어 정리

**forever 가 가진 명령어들은 크게 아래와 같습니다.**

```
 forever --help를 통해 forever에서 사용할 수 있는 명령어 옵션들을 알 수 있습니다.
```

**forever [start | stop | stopall | list | cleanlogs] [options] SCRIPT [script options]**

- start: script 를 데몬으로 시작
- stop: 데몬으로 시작한 script 중지
- stopall: 모든 forever scrtips 중지
- list: forever scripts 리스트 확인
- cleanlogs: forever 로그 파일 전부 삭제



### forever로 파이썬 실행하기

```
forever start -c python your_script.py
```

### Forever 끄기

```
forever stop your_script.py
```



**forever**로 파이썬을 실행하여 서버가 잘 작동되는지 확인하고 , 로컬에서 터미널을 끈 후에도 정상적으로 작동하는지 확인해본 후 정상적이라면 끝.