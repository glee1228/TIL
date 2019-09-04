## MS-DOS와 Linus 쉘 명령어 비교

| 명령어 사용 목적                          | MS-DOS      | Linux         | Linux 기본 예시                          |
| ----------------------------------------- | ----------- | ------------- | ---------------------------------------- |
| 파일 복사                                 | copy        | cp            | cp $$test.txt$$ $$/home/donghoon/$$      |
| 파일 이동                                 | move        | mv            | mv $$test.txt$$ $$/home/donghoon/$$      |
| 파일 목록보기                             | dir         | ls            | ls                                       |
| 스크린 깨끗이 지우기                      | cls         | clear         | clear                                    |
| 쉘 프롬프트 종료                          | exit        | exit          | exit                                     |
| 날짜 보기 또는 설정하기                   | date        | date          | date                                     |
| 파일 삭제                                 | del         | rm            | rm $$test.txt$$                          |
| 출력을 화면에 '반향하기'                  | echo        | echo          | echo $$this\ \ message$$                 |
| 단순 텍스트 편집기를 가지고 파일 편집하기 | edit        | gedit         | gedit $$test.txt $$                      |
| 파일 내용 비교                            | fc          | diff          | diff $$file1\ \ file2$$                  |
| 파일 내의 텍스트 문자열 찾기              | find        | grep          | grep  $$this\ contents$$    $$test.txt$$ |
| 디렉토리 만들기                           | mkdir       | mkdir         | mkdir $$directory\ name$$                |
| 파일 시스템에서 현재 위치 보기            | chdir       | pwd           | pwd                                      |
| 특정 경로로 디렉토리 바꾸기               | cd $$path$$ | cd  $$path $$ | cd $$/dir/dir$$                          |
| 상대 경로로 디렉토리 바꾸기               | cd ..       | cd ..         | cd ..                                    |
| RAM 사용량 보기                           | mem         | free          | free                                     |
|                                           |             |               |                                          |

