## 목요일 필기시험(9/13)

* Computational Thinking

* Call by Value, Call by Address

* Scope Rules
  * 지역 스코프 : 함수 내부에서 생성되는 스코프
  * 전역 스코프 : 모듈(파이썬 파일) 스코프
  * 내장 스코프 : 파이썬 자체 내장 영역 스코프

* OOP(Object Oriented Programming)

  * 컴퓨터 프로그래밍의 패러타임 중 하나

  * 기본 구성 요소 : 클래스(Class) , 객체(Object), 메소드(Method), 메세지(Message) 

  * 특징 :

    * 1. 자료 추상화 : 캡슐화(정보 은닉)

      2. 상속 : 기존의 클래스의 자료와 연산을 사용

      3. 다형성 : 오버라이딩과 오버로딩

      4. 동적 바인딩 : 런타임에 성격이 결정 

         ex) 런타임에 값에 따라 변수의 데이터 타입이 결정(python)

  * 객체 지향 언어 : 시뮬라 67, 스몰토크, 비주얼 베이직 닷넷, 오브젝티브-C, C++, C#, 자바, 객체지향 파스칼, 델파이, 파이썬, 펄, 루비, 액션스크립트, ASP, 스위프트

* Class

  * User-defined data type

    : 사용자가 데이터 타입을 정한다.

  * 클래스는 사용자가 데이터 타입을 정하는 것

  * 클래스 안에 있는 함수(Function)을 메소드(Method)라고 표현한다.

* Instance

  * Instance Variable
    * Instance 각각의 변수
  * Class Variable
    * Class 내의 공유하는 변수

  ```python
  >>> class Account:
          num_accounts = 0  #클래스 변수
          def __init__(self, name):
                  self.name = name
                  Account.num_accounts += 1 #객체가 생성될 때,num_accounts 개수를 1 증가시킴
          def __del__(self):
                  Account.num_accounts -= 1 #객체가 삭제될 때,num_accounts 개수를 1 감소시킴
  
  >>>
  ```


* inheritance
  * 클래스는 기반 클래스, 수퍼클래스, 또는 부모 클래스 등의 기존의 클래스로부터 속성과 동작을 상속받을수 있다
  * 서브 클래스
    * 
  * 수퍼 클래스

* Method Overriding

  * 상속관계 속의 클래스 내에서 메소드 이름과 매개변수 형태가 같을 경우, 수퍼클래스에서 정의된 메소드의 속성을 서브클래스에서 메소드 속성을 바꿔 쓸 수 있다.

  ```python
  class Thought(object):
      def __init__(self):
          pass
      def message(self):
          print "I feel like I am diagonally parked in a parallel universe."
  
  class Advice(Thought):
      def __init__(self):
          super(Advice, self).__init__()
      def message(self):
          print "Warning: Dates in calendar are closer than they appear"
          super(Advice, self).message()
  ```


* Operator Overloading

  * 연산자 중복
  * 사용자 정의 객체에서 필요한 연산자를 내장 타입과 형태와 동작이 유사하도록 재정의

  ```python
  
  ```


* Polymorphism
  * inheritance 관계 내의 다른 클래스들의 인스턴스들이 같은 멤버 함수 호출에 대해 각각 다르게 반응하도록 하는 기능
  * 상속과 다형성

* Constructor

