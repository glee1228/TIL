## 설치

### xrdp install

```
$ sudo apt install xrdp
```



### xfce4

```
$ sudo apt install xfce4
```



## 설정

### /etc/xrdp/startwm.sh 수정

```
#!/bin/sh

if [ -r /etc/default/locale ]; then . /etc/default/locale
export LANG LANGUAGE
fi
#xrdp multiple users configuration mate-session

#. /etc/X11/Xsession # -> 삭제 또는 주석처리
. /usr/startxfc4   -> 추가
```



### /etc/xrdp/xrdp.ini 수정

```
[gloabals]

~~~~~~
port=3389(default) -> 기본은 3389, 사용자가 열고자 하는 포트로 기재 ex)3389, 13000, etc..
~~~~~~
```



### /etc/xrdp/sesman.ini 

```
[globals]
~~~~~~
ListenPort=3350(default)
~~~~~~
```





### xrdp 오류 발생시

* 연결되어 있는 xrdp를 재시작한다. 

```
$ sudo service xrdp restart
```



* 위 명령어로 연결이 해제된 이후, openssh를 통해 연결하고자 하는 PC에 ssh로 접속한다.

```
$ ssh donghoon@49.167.9.202
```



* 연결이 되면, xrdp.ini 파일에 기재한 port번호와 sesman.ini에 기재한 ListenPort번호가 LISTEN 또는 established 상태로 할당되어 있는지 다음 명령어로 확인한다.

```
$ netstat -antp
```



* 만약 ListenPort 번호가 아래처럼 LISTEN 상태가 아닐경우, 다음 명령어로 서비스 재시작을 합니다.

```
tcp        0      0 127.0.0.1:3350          0.0.0.0:*               LISTEN      6714/sh
```



```
$ 	sudo systemctl restart xrdp
```

