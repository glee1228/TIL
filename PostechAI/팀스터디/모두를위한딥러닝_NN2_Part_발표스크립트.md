## Neural Network 2 : ReLU and 초기값 정하기

#### 시그모이드 보다 레루가 더 좋아!

* NN for XOR
  * 각 유닛의 시그모이드 함수가 붙어있는데 Activation Function이라고 한다.
    * 어느값 이상이면 Active가 되고 어느 값 이하면 작용하지 않는다.

* Let's go deep & wide!
  * X1,x2 로 x의 값이 두개이고, 출력하는 값이 [2,5]중 5이다.
  * 출력하고 그 뒤에서 다시 받고 받은 값을 다시 출력하는 식으로 진행
  * 마지막에 출력하는 값은 최종 원하는 개수에 맞게 출력한다.
  * 앞에 있는 것을 input layer라고 하고 마지막에 있는 것을 output layer라고 부른다.
  * 안에 있는것들은 보이지 않으므로 hidden layer라고 한다.
  * 특별한 의미는 없고 , 입력하고 출력에서 보이지 않기때문에 hidden layer라고 부른다.

* 9 hidden layers!
  * W1 = tf.Variable(tf.random_uniform[2,5],-1.0,1.0),name="weight1")
  * 의 input layer에서 입력값 2와 out layer에서 5에 해당하는 자리에 있는 숫자만 유의.
  * 그다음 할 일은 연결만 잘해주면 된다.
  * 최종 hypothesis까지 L1~L10까지 잘 연결하여 hypothesis에 L10을 input x로 지정한다.

* Tensorboard visualization
  * 텐서보드를 보면 그래프가 시각화 된다.
  * 연결 구조를 볼 수 있고 각각의 weight를 확인하고 잘되어있는지 확인이 가능.

* Poor results?
  * 코스트가 떨어지지 않고 최종 정확도가 0.5이다.
  * 한개의 레이어와 똑같다.

* Tensorboard Cost & Accuracy
  * 텐서보드를 통해 코스트와 정확도를 확인해보자.
  * 왜 이런 문제가발생할까?

* Backpropagation
  * 1986년도에 개발되면서 사람들이 흥분했다.
  * 2단 3단은 잘 학습되는데, 9단까지의 깊은 딥러닝에서는 학습이 안된다.
* Backpropagation (chain rule)
  * 미분을 하기위해 chain rule을 적용하여 나누어 미분값을 곱하여 최종 미분값을 추정한다.
  * f(g(x))에서 x에 대한 미분은 af/ax = (af/ag)/(ag/ax) 이다 .
  * 늘 시그모이드 함수를 통해 chain rule을 적용한 미분 값들의 곱하기는 결국 0보다 작은값들의 곱이므로 0에 수렴하게 된다.
  * 결국 input layer의 입력이 output layer에 영향을 거의 주지 않게 된다.
* Vanishing gradient
  * 경사도가 점점 사라지는 현상
  * 학습이 어려워진다.
  * 최종단 근처에 있는 어떤 경사와 기울기는 잘 나타나지만 처음부분의 경사와 기울기는 점점 희미해진다.
  * 1986~2006까지 이 문제로 인해 뉴럴네트워크가 잠자는 시기로 들어가게된다.
* Geoffrey hinton's summary of findings up to today
  * 시그모이드를 우리가 잘못 썼다!
* Sigmoid!
  * 1보다 작은값을 곱해나가다 보니 결국 최종적으로 너무 좋지않다.
  * 그와중에 생긴 함수가 ReLU이다.
  * 0보다 작으면? -> 끈다.
  * 0보다 크면 비례해서 커진다.
* ReLU : Rectified Linear Unit
  * 시그모이드 대신에 ReLU를 써라.
  * L1 = tf.sigmoid(tf.matmul(X,W1)+b1)
  * => L1 = tf.nn.relu(tf.matmul(X,W1)+b1)
* ReLU
  * 시그모이드 대신에 레루를 쓰고, 마지막 단에서는 시그모이드를 쓴다 -> 마지막에는 0또는 1이 출력되어야 하기때문에!!
* Works very well
  * 잘 된다
  * 레루가 중간 그래프에 들어가 있다.
  * 바로 학습을 시작하자마자 정확도가 1에 가까워지고 코스트가 0에 가까워진다.
* Cost function 
  * 시그모이드는 별로
* Activation Functions
  * 레루를 조금 진화시켜 리키레루를 만들었다.
  * 0보다 작은 지점은 좀더 주자.
  * ELU는 픽스된 값이 아닌 바뀐값으로 줘보자 
  * Maxout 은 약간 변형된 형태
  * Sigmoid를 0을 중심으로 -1에서 1사이의 값이 나오도록 변형시킨것은 tanh이다.
  * Sigmoid 거의 안쓴다.

#### Weight 초기화 잘해보자

* Vanishing gradient
  * 이문제를 해결하는 방법은 레루를 이용하는것.
  * 두 번째 방법은 
* Geoffrey Hinton/s summary of findings up to today
  * 초기값을 멍청하게 했으니 제대로 하자.
* Cost function
  * 레루를 가지고 사용해도 초기값이 잘못되니 잘 안떨어진다.
* Set all initial weights to 0
  * 초기값을 쿨하게 0으로 줘보자
  * 어떤 문제 ? 
  * w를 0으로 줘버리면, x에서 forward propagation할 때 기울기를 곱할때 전부다 0이 된다.
  * 결국 gradient가 사라져버린다.
* Need to set the initial weight values wisely
  * 절대 초기값 0은 주지마라!
  * 어려운 문제다
  * RBM이라는 것을 사용해 초기값을 정해보았다 2006년에
* RBM Structure
  * 어떻게 동작되는것일까?
  * 여기서 입력과 출력단만 있다고 치자
  * 입력을 재생산하는 내용이다.
  * forward에 어떤 입력이 있다고 치면, weight와 b를 가지고 곱해서 어떤 값을 내는것을 forward라고 한다. 각각의 어떤 값을 만들어낸다. 이값에 따라 어떤경우엔 이 값이 크게 작용하고 이런 과정을 통해 값을 보낸다
  * 두 번째는 이 weight를 반대로 사용한다. 이 weight를 거꾸로 쏴준다. 뭘 비교하냐하면, 이 첫 번째 줬던 값을 받은 값과 생성된 x의 값과 비교한다.이 값의 차이가 최저가 되도록 weight를 조절한다. 비슷한 형태의 값이 나오게 이 weight를 조정하게 하는것을 Restrict boltzman이라고 한다. 이값을 거꾸로 쓰면 다시 돌아온다. 이값을 오프인코더 오프디코더라고 한다.
  * 이것을 갖고 weight를 초기화시킨다.
* How can we use RBM to initialize weights?
  * 초기값을 내가 준값과 유사하게 학습시킨다.
  * Deep Belief Network
  * PreTraining 
    * x라는 값이 있을 때 RBM을 돌린다.
    * x와 유사한 값이 나오는 weight를 학습시키자
    * 앞과 뒤의 레이어만 갖고 입력된 x의 값이 나오는 weight를 학습시키자
    * 전체 네트워크를 보면 weight값이 들어있다. 이 값들이 초기화 된 값이다.
    *  실제 레이블을 놓고 학습을 시키면 빠르게 학습이 된다.
    * 이것을 fine tunning 이라고 한다.
* Good news
  * 좋은 소식은 간단한 초기값을 줘도 된다는 것을 알아냈다.
  * Xavier initialization 이 나왔다.
  * 식을 한번 보자. 
  * W = np.random.randn(fan_in,fan_out)/np.sqrt(fan_in)
  * 2015년도에 -> W = np.random.randn(fan_in,fan_out)/np.sqrt(fan_in/2)
* Prettytensor implementation
  * 실습시간에 코드 구현
* Activation functions and initialization on CIFAR-10
  * 조금 차이가 있긴 한데. 연구자들이 여러가지 방법으로 해보았다. 초기화방법을 참고
* Still an active area of research
  * 우리가 모른다. 어떻게 완벽한 초기값을 세팅할수있을지.
  * 많은 알고리즘이 있다. 
  * 배치노말라이제이션, 레이어시퀀셜유니폼 베리언스 등등...
* Geoffrey Hinton's summary of findings up to today
  * 우리의 라벨링된 데이터 셋들이 너무 적다
  * 우리의 컴퓨터가 너무 느리다.
  * 우리는 weight 초기화를 제대로 못했다.
  * 우리는 틀린 비선형 타입을 사용했다.

#### Dropout 과 모델 앙상블

* 오버피팅 : 간단한 데이터가 있을 때 , 좋은 커브로 할 때 잘 맞다고 하는데, 식을 매우 꼬브려서 학습데이터 외에 테스트데이터를 넣었을떄 정확도가 떨어지는 경우 오버피팅되었다고 한다.

* Am I overfitting?

  * 어떤 문제가 있나?
  * 에러가 떨어진다. -> 잘되다가 -> 실전데이터를 사용하면 -> 에러가 다시 올라간다.
  * 에러가 올라가는 지점부터 overfitting이라고 한다.
  * 깊게 만들수록 overfitting이 될 가능성이 높아진다.

* Solutions for overfitting

  * 학습데이터가 더 많을수록 오버피팅이 방지된다.

* Regularzation

  * 너무 많은 숫자들이 weight에 존재하지않게 하자!
    * l2reg = 0.001*tf.reduce_sum(tf.square(W))
  * 레귤러제이션을 사용하여 범주를 좁혀 정규화하자

* Dropout : A simple Way to Prevent Neural Networks from Overfitting

  * 뉴럴네트워크를 엮었는데, 임의로 끊자!

  * 몇개의 노드를 죽이자

  * 랜덤하게 어떤 뉴런들을 죽여버리잨ㅋㅋ

  * 될까? 근데 잘된다 ㅋㅋㅋㅋㅋㅋㅋ

  * 각각의 뉴런들은 전문가들이다. 훈련할 때 몇명은 쉬어라~ 남은 사람들 갖고 훈련한다. 쉬게하면서 훈련을 시킨다. 어떤 뉴런이 귀가있는지 꼬리가 있는지 보는데, 몇명을 쉬게한다. 나머지 사람들만 갖고 맞추게 한다.ㅎㅎ 나중엔 그 전문가들을 총 동원해서 인식하게 한다 ㅋㅋㅋㅋㅋㅋㅋ 잘됌

  * TensorFlow implementation

    * dropout_rate = tf.placeholder("float")

      _L1 = tf.nn.relu(tf.add(tf.matmul(X,W1),B1))

      L1=tf.nn.dropout(_L1,dropout_rate)

    * 훈련에는 드랍아웃을 0.5에서 0.7

    * 실전 평가나 실제 모델을 사용할땐 드랍아웃을 1로 해!!!

  * What is Ensemble?

    * 내가 독립적으로 뉴럴 네트워크를 만들때 , 9단의 뉴럴네트워크를 만들었다고 치고 3개의 모델을 각각 학습시킨다 하면, 결과가 각각마다 조금씩 다르다.그리고 마지막에 합쳐서 결과를 낸다. 전문가 한명에게 물어보는 것보다 독립된 전문가 여러명에게 물어보는게 조금더 잘 할수도 있다.
    * 2~4,5%까지 정확도를 향상시킬수있다.

#### 레고처럼 넷트웍 모듈을 마음껏 쌓아보자

* Feedforward neural network
  * 내가원하는대로 쌓아올린다 ㅎㅎ
* Fast forward : 단순한 forward 네트워크를 볼수 있다. 중간 나오는 출력을 뽑아서 2단 앞에서 출력시킬 수 있다. 이런 시그널을 앞으로 잡아당겨서 사이에 들어가게 만들수 있다. 3%이하로 만들어줬던 NesNet이라는 구조이다.
* Split & merge : x를 하나에 넣고 두개로 나눠서 가다가 또 만나고 다시 또 나눠질 수도 있는 구조를 만들기도 하고 x입력을 나눠서 넣고 각각을 처리하고 다시 합쳐서 Y를 예측하는 구조도 있다. 이것을 Convolution Neural Network라고 한다.
* Recurrent Network : 앞으로 쭉 나가다가 옆으로 나가고 옆으로 나갔다가 앞으로 나갔다가 하면서 하는 구조를 RNN이라고 한다. 



#### 딥러닝으로 MNIST 98%이상 해보기

* Softmax classifier for MNIST 

  * 손으로 쓴 글씨를 소프트맥스로 알아맞히는 것을 해보았다.
  * 784개의 벡터가 있고 그것을 10개로 출력하는 W를 랜덤하게 설정
  * 지난 시간에 배치사이즈를 학습해보았다.
  * 각 에폭마다 코스트가 나오고 마지막에 정확도가 나오는데, 90퍼센트가 나왔다.

* NN for MNIST

  * 좀 더 깊게 들어간다. 
  * 단을 추가하여서 W의 크기를 구하는 것인데, 784개를 입력받아 256개를 출력한다.
  * 처음에 784개가 들어가고 몇단을 구성해서 제일 마지막엔 10개가 확정된다.
  * 중간에 몇개가 나올건지는 디자인 하기 나름.
  * 우리는 256개로 만들고, 받을때도 256개를 받고 쏜다.
  * 출력도 256개로 한다. 
  * 마지막은 10개로 정해져있다. 0~9까지의 숫자이므로
  * X가 입력이 되고 L1이 입력이 되고 L2가 입력이 된다.
  * relu를 사용하고, (시그모이드 X)
  * 정확도가 94%가 되었다!!

* Xavier initialization

  * 구글에 가서 샤비에 이니셜라이제이션 텐서플로 검색해보면 나온다.
  * 이 과정은 초기화값을 가장 최적의 값을 찾아 학습속도와 결과를 최적화 시키는 방법이다. 
  * 똑같이 3단만 사용하고 W1,W2,W3부분의 이니셜라이저 부분만 샤비에이니셜라이즈를 추가한다.
  * 결과는 놀랍게도 97.8%!!!

* Xavier for MNIST

  * 초기값이 잘 이니셜 되었다.
  * 94퍼센트에서 97퍼센트로 급격히 성능이 향상되었다.

* Deep NN for MNIST

  * 5단으로 늘리고
  * 256개로 출력했는데 512개로 늘리자
  * 샤비에 이니셜라이즈도 물론 쓴다.
  * 결과는 실망... 97.4%가 나왔다.
  * 이유가 뭘까?
  * 데이터마다 다른 요인이 있지만 , 아마도 오버피팅이 요인일듯하다.....
  * 네트워크들이 학습데이터들을 너무 잘 기억해버려서 새로운 테스트데이터가 들어왔을때 오히려 결과가 나빠질수있다.

* Dropout for MNIST

  * Dropout을 사용한다.
  * 한 레이어를 더 넣어준다 
  * L1 = tf.nn.relu(tf.matmul(X,W1)+b1)
  * L1 =tf.nn.dropout(L1,keep_prob=keep_prob)
  * 드랍아웃 한줄을 추가해준다. 
  * 학습할 때는 Keep_prob: 0.7
  * 테스팅할 때는 반드시 Keep_prob: 1 !!
  * 결과는 놀랍게 98%!!!

* Optimizers

  * 많은 옵티마이저가 있다. 
  * 그래디언트디센트말고도~!!

* ADAM : a method for stochastic optimization

  * 아담이 제일 좋다. 처음에는 아담으로 해봐라~
  * optimizer = tf.train.AdamOptimizer(learning_rate=learning_rate).minimize(cost)

* Summary

  * 간단한 소프트맥스 vs 뉴럴넷워크 -> 성능 향상
  * 샤비에 이니셜라이제이션 : 성능향상
  * 드랍아웃 : 성능향상
  * 아담과 그외의 옵티마이저 : 성능향상
  * 최근들어 배치 노말라이제이션을 많이 쓰는데, 깃허브에 있다.
