## CRONTAB 으로 특정 url에 자동요청 보내기

1. .sh 파일 만들기

```
$ vi chatbot.sh
```

2. Curl 명령어로 특정 url에 요청보내는 스크립트 작성 (chatbot.sh)

```
#! /bin/bash
curl https://pychat3.herokuapp.com
```

* 보통 스크립트의 경우에는 상단에 쉬뱅 작성

3. 크론탭 편집하기 

```
$ crontab -e
```

4. 크론탭 내용 추가하기(로그 포함)

```
* * * * /Users/donghoon/chatbot.sh > /Users/donghoon/chatbot.log 2>&1
```

* 매 시간 0분 20분 40분 마다 실행 시키고 싶을 경우

```
0,20,40 * * * * /Users/donghoon/chatbot.sh > /Users/donghoon/chatbot.log 2>&1
```

5. 스크립트 권한 부여(쉘 스크립트 실행을 위해)

```
chmod +x chatbot.sh
```

* chmod로 permission 세팅하기