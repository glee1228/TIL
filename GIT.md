## Git

> Git이란, 분산버전관리시스템(DVCS)이다. 

1. 저장소로 만들기

   1. 내 로컬 프로젝트 폴더에서 아래의 명령어를 입력한다.

      ```
      $ git init
      Initialized empty Git repository in C:/Program Files/Git/test/.git/
      ```

   2. 원격저장소에 있는 저장소를 가져오기

      ```
      $ git clone __url__
      ```


2. 저장소 활용하기

   1. `워킹트리(working tree)` 에 변경된 사항들을`인덱스(Staging Area)` 로 이동
      Staging Area는 `커밋(commit)` 대상 파일들이다.

      ```
      $ git add . 
      $ git add 파일명/디렉토리
      ```

   2. 커밋!

      ```
      $ git commit -m '커밋내용'
      ```

      커밋 이력 확인 하기
      ```
      $ git log
      commit 555e2f9d121f8a182e0e507e2d7cbcb66c7d8220 (HEAD -> master)
      Author: 7akikim <takfeb@gmail.com>
      Date:   Wed Aug 29 09:29:08 2018 +0900
      
          b.txt 추가
      
      ```



3. 원격 저장소 활용하기

   1. 원격 저장소 설정

      ```
      $ git remote add origin __주소__
      ```

      * remote 저장소를 origin이라는 이름으로 추가한다.

   2. 원격 저장소로 `push`

      ```
      $ git push origin master
      ```

      * `origin 원격 저장소`로 `master 브랜치`를 `push`

   3. 원격 저장소에서 `pull`

      ```
      $ git pull origin master
      ```

      * `origin 원격 저장소`에서 `master 브랜치`로 가져오기(`pull`)
      * 주의사항! 커밋 이력이 다를 경우 충돌 날 수 있음.

* 추가 명령어

  * git 상태 확인하기 

    ```
    $ git stauts
    ```

  * 커밋 이력 확인하기 

    ```
    $ git log -n 5
    ```

  * 원격저장소 확인하기

    ```
    $ git remote -v
    ```

* [Git 입문](https://backlog.com/git-tutorial/kr/)
* [Git scm 한글문서](https://git-scm.com/book/ko/v1/%EC%8B%9C%EC%9E%91%ED%95%98%EA%B8%B0)
* [git 토끼와 거북이](https://milooy.wordpress.com/2017/06/21/working-together-with-github-tutorial/)