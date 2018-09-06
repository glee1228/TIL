### 수업내용

<hr>

```
# : 전처리 지시자 inlcude : 포함시키다 <stdio.h> : stdio.h 헤더파일
#include<stdio.h>
```



### Divide conquer 

<hr>

* 분할 정복 알고리즘**(Divide and conquer algorithm)은 그대로 해결할 수 없는 문제를 작은 문제로 분할하여 문제를 해결하는 방법이나 [알고리즘](https://ko.wikipedia.org/wiki/%EC%95%8C%EA%B3%A0%EB%A6%AC%EC%A6%98)이다.

* [빠른 정렬](https://ko.wikipedia.org/wiki/%EB%B9%A0%EB%A5%B8_%EC%A0%95%EB%A0%AC)이나 [합병 정렬](https://ko.wikipedia.org/wiki/%ED%95%A9%EB%B3%91_%EC%A0%95%EB%A0%AC)로 대표되는 [정렬 알고리즘](https://ko.wikipedia.org/wiki/%EC%A0%95%EB%A0%AC_%EC%95%8C%EA%B3%A0%EB%A6%AC%EC%A6%98) 문제와 [고속 푸리에 변환](https://ko.wikipedia.org/wiki/%EA%B3%A0%EC%86%8D_%ED%91%B8%EB%A6%AC%EC%97%90_%EB%B3%80%ED%99%98)(FFT) 문제가 대표적이다.

## 분할 정복 알고리즘

분할 정복 알고리즘은 보통 [재귀 함수](https://ko.wikipedia.org/wiki/%EC%9E%AC%EA%B7%80_%ED%95%A8%EC%88%98)(recursive function)를 통해 자연스럽게 구현된다. 예를 들면,

```
function F(x):
  if F(x)의 문제가 간단 then:
    return F(x)을 직접 계산한 값
  else:
    x 를 y1, y2로 분할
    F(y1)과 F(y2)를 호출
    return F(y1), F(y2)로부터 F(x)를 구한 값
```

또한 여기서 작은 부문제로 분할할 경우에 부문제를 푸는 알고리즘은 임의로 선택할 수 있다. 이러한 재귀호출을 사용한 함수는 함수 호출 오버헤드 때문에 실행 속도가 늦어진다.

빠른 실행이나 부문제 해결 순서 선택을 위해, 재귀호출을 사용하지 않고 [스택](https://ko.wikipedia.org/wiki/%EC%8A%A4%ED%83%9D), [큐](https://ko.wikipedia.org/wiki/%ED%81%90_(%EC%9E%90%EB%A3%8C_%EA%B5%AC%EC%A1%B0))(queue) 등의 [자료구조](https://ko.wikipedia.org/wiki/%EC%9E%90%EB%A3%8C%EA%B5%AC%EC%A1%B0)를 이용하여 분할 정복법을 구현하는 것도 가능하다.



### 동적 타이핑(dynamic typing)

<hr>

```python
a = 1 ;					print(id(a))
a = 1.5; 				print(id(a))
a = 'a'; 				print(id(a))
a = "hello world!"; 	print(id(a))
```

```
1856682448
2331000664688
2330963603048
2331002601200
```

* 값을 다른 변수 형태로 저장할 때마다 id가 변한다.



```python
a = 1;		print(id(a))
b = 1;		print(id(a))
c = 2;		print(id(a))
d = 2;		print(id(a))
```

```
1856682448
1856682448
1856682480
1856682480
```

* 변수 타입과 변수의 값이 같을 경우, id는 같다
* 변수 타입은 같지만 변수의 값이 다를 경우, id는 다르다



### Class(클래스)

<hr>

#### : User Defined Data Type

C언어의 구조체 : 변수 집합만 정의 

자바와 C++의 클래스 : 변수 집합과 메소드 집합을 정의

객체 : 클래스의 변수



### 언어의 성격

<hr>

* C -절차 지향
* 자바 - 객체 지향
* 파이썬 - 하이브리드 언어(절차지향 & 객체지향)



### C언의 scanf와 파이썬의 input의 차이점

<hr>

```C
#include<stdio.h>
void main(){
       int a;
       scanf("%d", &a);
       printf("%d", a);
}
```

* C에서 입력은 입력받는 변수를 선언하고 그 변수의 타입을 지정한다.

```python
a = input("입력 : ")
print(a)   
```

* 파이썬에서 입력은 입력받는 변수가 default로 String으로 지정되어있다.



### 정적 할당과 동적 할당(?) - 내용 수정 필요

<hr>

stack 영역의 포인터를 선언하고 heap영역의 객체를 생성

stack영역의 포인터가 heap영역의 객체를 가리킨다.





### 스택 구조와 큐 구조

<hr>

* 스택은 선입후출

* 큐는 선입선출



### Call by Value & Call by Address

<hr>

* C에서는 함수를 호출했을 때 메모리를 사용하고 사용이 끝나면 메모리를 반환한다.
* Call by Value에서는 원본의 값을 바꾸지않는다
* Call by Address에서는 원본의 주소를 참조하기 때문에 값에 접근가능하다.
* C에서는 함수에서 return 값을 한개만 가져올 수 있다는 제약이 있기 때문에, 두 개의 변수를 Swap할 경우 등등에는 Call by Address를 사용한다.



### 파이썬 함수 이용할 때 주의할 점

<hr>

1. 파이썬 인터프리터가 실행될 때 함수가 먼저 실행되지 않음. 절차 지향으로 위에서 아래로 실행하므로 함수 호출은 함수 선언 아래에서 해야 한다.

2. 함수 작성 예시

   ```python
   def main():
       print(power(10,2))
       
   def power(x,y):
       result = 1
       for i in range(y):
           result = result * x
       return result
   
   main()
   ```

   출력결과:

   ```
   100
   ```


