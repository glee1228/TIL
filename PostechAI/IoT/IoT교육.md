## Iot 교육 

* 실습 위주의 교육 
* 압축된 강의내용

<hr></hr>



### KEYSIGHT(technologies)

* 전자 관련한 전공 설명
* 휴렛 패커드
  * 계측 기기 최초 회사
* Agilent Technology(99~13)
* Keysight(13~)
* 외부 환경과 통신하고 상호 작용하는 임베디드 기술이 포함된 물리적 개체 네트워크 - IoT
* M2M 
  * 기기와 기기간의 연결을 통한 산업적 형태 (Machine To Machine)
  * 수동적 형태(hardware dependent)

* IoT
  * 서비스와 물체 사이의 웹이 포함
  * 독단적 연결이 아닌 모든 사물이 RPA 네트워크를 이용해 연결(Internet of Things)
  * 적극적 형태(software dependent)
* Fixed Internet -> Mobile Internet -> Internet of Things
* 일단 연결하고 빅데이터를 생산하고 가공해서 추론하고 판단해서 유용한 부가가치가 있는 서비스를 만들어내는데 목적이 있음
* IoT -> Big Data -> AI
  * 데이터 수집 -> 데이터 추출 및 적재 , 분석 -> 데이터 기반 학습
* 제조 프로세스(카메라), 모빌리티(차량 센서, 스마트폰) , 스마트 하우스(가전 제품, 스마트미터), 의료 건강(바이탈 센서), 인프라(모니터링 센서)
* Hype Cycle 참조(주제 선정에 있어)
  * Autonomous Things(자율 사물)
  * Empowered Edge(엣지 컴퓨팅)
  * AI,Driven Development(자율주행 발전)
  * Quantum Computing(양자 컴퓨팅)
  * Digital Twins(디지털 트윈)
    * 컴퓨테에 현실 속 사무르이 쌍둥이를 만들고, 현실에서 발생할 수 있는 상황을 컴퓨터로 시뮬레이션함으로서 결과를 미리 예측하는 기술
  * IoT Architecture
    * Device Layer
      * Industrial -> Industrial Gateway
      * Home -> Consumer Gateway
      * Wearable -> SmartPhone
    * Connectivity layer
      * Internet
    * Data Center & App Layer
      * Server cluster
* 주제 선정 풀
  * Gartner
  * CISCO
  * ERICSSON
* IoT에서 가장 중요한 미션들
  * 강한 퍼포먼스
  * 정확도
  * 신뢰도
  * 안전성
  * 적은 지연성
  * 새로운 프로세스를 지원하는 능력
* IoT 분야
  * 생산관리, 헬스케어, 기름,가스,에너지, 운송, 농업
* 디자인 최적화
  * 아래의 것들을 모두 전체적으로 만족해야한다.
    * 소프트웨어 안정성
    * 마켓을 위한 시간
    * 적은 코스트
    * 적은 전력
    * 데이터 최대치
    * 하드웨어 의존성
* IoT 디바이스에서 갖추어야 할것
  * 센서
    * 계측의 정확성 
  * 에너지
    * 파워 소모량
  * 무선
* IoT Block Diagram
  * 베터리
  * 파워 관리
  * MCU
  * RF
  * Interface
  * Analog Frontend
  * Actuator/Display
  * Sensor
* Sensors 
  * 물리적 파라미터
    * 온도
    * 위치
    * 가속도
    * 방향
    * 위치
    * 압력
  * 전자 시그널
    * DC &AC volts
    * DC & AC current
    * Resistance
    * Capacitance
    * Frequency
    * Phase
* Energy
  * 간헐적인 동작이나 띄엄띄엄 데이터를 전송하는 경우가 많기 때문에 전류 소모가 슬립모드와 동작모드가 공존하는 형태로 존재한다.(저전력 소비를 위해)
* Power Integrity
  * 무어의 법칙 
  * IC 직접도가 늘어나면서 더 높은 효율성을 개발자에게 요구한다.
* Wireless : 어떻게 하면 상호호환성이 있을까
  * 다양한 무선 접속 기술이 존재
  * 다양한 기술들이 서비스 되고 있는데, 어떤 기기가 올바르게 동작할 것인가
* 공존/ 간섭신호 (Coexistence & Interference)
  * 의료기기에서 중요
  * 다른 기기 사이에서의 간섭 신호에서 내 기기의 신호를  잘 받을 수 있는가

* 블루투스 5.0
  * 블루투스 4.2에 비해 대역폭이 2배 
  * 블루투스 4.2에 비해 거리는 4배
  * 블루투스 4.2에 비해 메세지 용량은 8배
* IEEE 802.11 
  * 현재 주로 쓰이는 유선 LAN 형태인 [이더넷](https://ko.wikipedia.org/wiki/%EC%9D%B4%EB%8D%94%EB%84%B7)의 단점을 보완하기 위해 고안된 기술로, 이더넷 네트워크의 말단에 위치해 필요 없는 배선 작업과 유지관리 비용을 최소화하기 위해 널리 쓰이고 있다. 보통 폐쇄되지 않은 넓은 공간(예를 들어, 하나의 사무실)에 하나의 핫스팟을 설치하며, 외부 [WAN](https://ko.wikipedia.org/wiki/WAN)과 [백본 스위치](https://ko.wikipedia.org/w/index.php?title=%EB%B0%B1%EB%B3%B8_%EC%8A%A4%EC%9C%84%EC%B9%98&action=edit&redlink=1), 각 사무실 [핫스팟](https://ko.wikipedia.org/wiki/%ED%95%AB%EC%8A%A4%ED%8C%9F_(%EC%99%80%EC%9D%B4%ED%8C%8C%EC%9D%B4)) 사이를 이더넷 네트워크로 연결하고, 핫스팟부터 각 사무실의 컴퓨터는 무선으로 연결함으로써 사무실 내에 번거로이 케이블을 설치하고 유지보수를 하지 않아도 된다.
* Smart Home
  * 무호흡에 반응하는 침대
  * 물 섭취량에 대해 피드백주는 정수기
* Smart City
  * 개체의 효율성을 늘려 전체의 효율성을 늘리는 방향
  * 효율적인 도시관리를 전체적으로 하면, 전체의 cost가 내려가게 됨
  * LPWA Technologies
    * 가로등
    * 파킹 스페이스
    * 쓰레기 수거
    * 농업
    * 산불 모니터링
  * LPWAN
    * 사용 범위
      - 거리는 길고, 데이터양과 전력 소비는 적을 때
  * LoRa(Long Range)
    * 블랙박스에서 찍은 영상을 인터넷에서 활용
* IoT 관련 information
  * www.keysight.com/find/iot
* Maximizing IoT Device Battery Life

