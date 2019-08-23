## Mac 환경에서 VSCode 설치, C 코드 디버깅하기

glee1228@naver.com



### 디버거(Debugger)란?

응용 소프트웨어 프로그램을 디버깅하고 프로그램 실행 중 발생하는 상황을 분석하는 데 도움을 줍니다. 

디버거(Debugger)의 역할은 크게 3가지입니다.

1. 조건을 지정하여 프로그램을 실행하고 중지 또는 일시정지할 수 있습니다
2. 프로그램 일시 정지한 후, 상태 분석 및 변수, 레지스터 값을 확인할 수 있습니다
3. 변수와 레지스터 값을 변경하여 프로그램 동작에 미치는 영향을 확인하고 소스 코드를 수정하지 않고도 수행할 수 있습니다.

간단히 말해, 버그 원인을 찾기 위해 사용하는 것이 디버거(Debugger)입니다.



그럼 Mac 환경에서 VSCode C코드를 디버깅해봅시다.



### VSCode 설치

https://code.visualstudio.com/

![image-20190824004838346](/Users/donghoon/Library/Application Support/typora-user-images/image-20190824004838346.png)



### UI 한글로 변경

1. 왼쪽 블록모양의 메뉴 클릭한 후, 'Korean Language Pack for Visual Studio Code' 설치

![image-20190824004305099](/Users/donghoon/Library/Application Support/typora-user-images/image-20190824004305099.png)

2. command + shift + p 입력

3. 'display' 입력 후 ko 선택

![image-20190824004617647](/Users/donghoon/Library/Application Support/typora-user-images/image-20190824004617647.png)

![image-20190824004654087](/Users/donghoon/Library/Application Support/typora-user-images/image-20190824004654087.png)

4. 다시 시작 버튼을 누르면, VSCode 재시작 후 한글로 UI가 변경됨.

![image-20190824004727478](/Users/donghoon/Library/Application Support/typora-user-images/image-20190824004727478.png)



### C/C++ 확장팩 설치

![image-20190824005732726](/Users/donghoon/Library/Application Support/typora-user-images/image-20190824005732726.png)



### 프로젝트 만들기

1. 프로젝트를 저장하고자 하는 곳에 새로운 폴더를 생성한다.
2. 폴더 열기를 클릭해 해당 폴더를 연다.
3. stack.c 로 파일명을 저장한다(우린 c로 짠 stack 코드를 디버깅할거니깐)



stack.c

```c
#include <stdio.h>
#include <stdlib.h>

#define MAX 10

int STACK[MAX], TOP;
/* display stack element*/
void display(int[]);

/* push (insert) item into stack*/
void PUSH(int[], int);

/* pop (remove) item from stack*/
void POP(int[]);

int main()
{
    int ITEM = 0;
    int choice = 0;
    TOP = -1;

    while (1)
    {
        printf("Enter Choice (1: display, 2: insert (PUSH), 3: remove(POP)), 4: Exit..:");
        scanf("%d", &choice);

        switch (choice)
        {
        case 1:
            display(STACK);
            break;
        case 2:
            printf("Enter Item to be insert :");
            scanf("%d", &ITEM);
            PUSH(STACK, ITEM);
            break;
        case 3:
            POP(STACK);
            break;
        case 4:
            exit(0);
        default:
            printf("\nInvalid choice.");
            break;
        }
        int _getch();
    } // end of while(1)
}

/*  function    : display(),
    to display stack elements.
*/
void display(int stack[])
{
    int i = 0;
    if (TOP == -1)
    {
        printf("Stack is Empty .\n");
        return;
    }

    printf("%d <-- TOP ", stack[TOP]);
    for (i = TOP - 1; i >= 0; i--)
    {
        printf("\n%d", stack[i]);
    }
    printf("\n\n");
}

/*  function    : PUSH(),
    to push an item into stack.
*/
void PUSH(int stack[], int item)
{
    if (TOP == MAX - 1)
    {
        printf("\nSTACK is FULL CAN't ADD ITEM\n");
        return;
    }
    TOP++;
    stack[TOP] = item;
}

/*  function    : POP(),
    to pop an item from stack.
*/
void POP(int stack[])
{
    int deletedItem;
    if (TOP == -1)
    {
        printf("STACK is EMPTY.\n");
        return;
    }

    deletedItem = stack[TOP];
    TOP--;
    printf("%d deleted successfully\n", deletedItem);
    return;
}

```



### 컴파일에 필요한 tasks.json 만들기

1. 상단 바에서 터미널 ->  '기본빌드 작업구성..' 선택
2. '템플릿에서 tasks.json 파일 만들기' 선택
3. 'Others 임의의 외부 명령을 실행하는 예' 선택
4. tasks.json 코드는 아래로 저장한다.

tasks.json

```json
{
    "version": "2.0.0",
    "runner": "terminal",
    "type": "shell",
    "echoCommand": true,
    "presentation": {
        "reveal": "always"
    },
    "tasks": [
        //C++ 컴파일
        {
            "label": "save and compile for C++",
            "command": "g++",
            "args": [
                "${file}",
                "-std=c++11",
                "-o",
                "${fileDirname}/${fileBasenameNoExtension}"
            ],
            "group": "build",
            //컴파일시 에러를 편집기에 반영
            //참고:   https://code.visualstudio.com/docs/editor/tasks#_defining-a-problem-matcher
            "problemMatcher": {
                "fileLocation": [
                    "relative",
                    "${workspaceRoot}"
                ],
                "pattern": {
                    // The regular expression. 
                    //Example to match: helloWorld.c:5:3: warning: implicit declaration of function 'prinft'
                    "regexp": "^(.*):(\\d+):(\\d+):\\s+(warning error):\\s+(.*)$",
                    "file": 1,
                    "line": 2,
                    "column": 3,
                    "severity": 4,
                    "message": 5
                }
            }
        },
        //C 컴파일
        {
            "label": "save and compile for C",
            "command": "gcc",
            "args": [
                "${file}",
                "-o",
                "${fileDirname}/${fileBasenameNoExtension}"
            ],
            "group": "build",
            //컴파일시 에러를 편집기에 반영
            //참고:   https://code.visualstudio.com/docs/editor/tasks#_defining-a-problem-matcher
            "problemMatcher": {
                "fileLocation": [
                    "relative",
                    "${workspaceRoot}"
                ],
                "pattern": {
                    // The regular expression. 
                    //Example to match: helloWorld.c:5:3: warning: implicit declaration of function 'prinft'
                    "regexp": "^(.*):(\\d+):(\\d+):\\s+(warning error):\\s+(.*)$",
                    "file": 1,
                    "line": 2,
                    "column": 3,
                    "severity": 4,
                    "message": 5
                }
            }
        },
        // 바이너리 실행(Ubuntu)
        {
            "label": "execute",
            "command": "cd ${fileDirname} && ./${fileBasenameNoExtension}",
            "group": "test"
        }
        // // 바이너리 실행(Windows)
        // {
        //     "label": "execute",
        //     "command": "cmd",
        //     "group": "test",
        //     "args": [
        //         "/C", "${fileDirname}\\${fileBasenameNoExtension}"
        //     ]
        // }
    ]
}
```





### 디버깅을 위한 gdb설치 및 gcc 명령어 그리고  launch.json 만들기

1. gdb 디버깅 패키지를 brew 명령어로 설치해줍니다. 

![image-20190824011534373](/Users/donghoon/Library/Application Support/typora-user-images/image-20190824011534373.png)

gcc와 gdb가 아직 잘 모르시는 분들은 다음 링크를 참조하세요.

[Tutorial of gcc and gdb(Eng)](http://cseweb.ucsd.edu/classes/fa09/cse141/tutorial_gcc_gdb.html)



2. VSCode 왼쪽 메뉴중 벌레모양(Debug) 메뉴 선택 -> 톱니바퀴 선택

![image-20190824013240693](/Users/donghoon/Library/Application Support/typora-user-images/image-20190824013240693.png)

3. GDB/LLDB 선택

![image-20190824013418631](/Users/donghoon/Library/Application Support/typora-user-images/image-20190824013418631.png)

4. launch.json에 아래 내용과 동일하게 수정

launch.json

```json
{
    "version": "0.2.0",
    "configurations": [
        {
            "name": "(gdb) Launch",
            "type": "cppdbg",
            "request": "launch",
            "program": "${fileDirname}/a.out",
            "args": [],
            "stopAtEntry": false,
            "cwd": "${workspaceFolder}",
            "environment": [],
            "externalConsole": true,
            "MIMode": "gdb"
        }
    ]
}
```



5. 터미널 cd 명령어로 stack.c 파일이 있는 디렉토리로 이동(제 Mac에서의 경로는 다음과 같이GitHub/TIL/Algorithm/C_basic 이므로 개인 pc에 맞추어 경로를 지정하시면 됩니다)

![image-20190824014059566](/Users/donghoon/Library/Application Support/typora-user-images/image-20190824014059566.png)

6. gcc 에 -g 옵션을 주어 gdb에게 제공하는 정보를 바이너리에 삽입합니다.

   (-g 옵션은 디버깅 옵션입니다. 만약 -g를 사용하지 않고 gdb로 디버깅하면, 역어셈 - > 어셈블리 코드로만 디버깅이 가능합니다)

![image-20190824014501990](/Users/donghoon/Library/Application Support/typora-user-images/image-20190824014501990.png)

7. 아래와 같이 중단점을 찍고, F5를 눌러 코드 디버깅을 하면 됩니다.

![image-20190824014628727](/Users/donghoon/Library/Application Support/typora-user-images/image-20190824014628727.png)

![image-20190824014713534](/Users/donghoon/Library/Application Support/typora-user-images/image-20190824014713534.png)