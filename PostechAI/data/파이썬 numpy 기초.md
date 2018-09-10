## Numpy 란?

: 행렬(Matrix) 및 Tensor 연산을 쉽고 빠르게 해주는 Python의 라이브러리



Tensorflow, Theano 등의 주요 NN 라이브러리에서 데이터 관련 작업 시 직접 활용하게 됨



### numpy.array

<hr>

1. 배열 값을 명시해서 생성하는 방법

```python
import numpy as np

a = np.array([1,2,3]) # 1차원 array [1,2,3] 생성

print(type(a))
print(a.shape)
print(a[0], a[1], a[2])
a[0] = 5
print(a)
b = np.array([[1,2,3],[4,5,6]])
print(b.shape)
print(b[0, 0], b[0, 1], b[1, 0])
```



2. 배열 값을 명시하지 않고 생성하는 방법

```python
import numpy as np

a = np.zeros((2,2)) # 모든 값이 0인 2x2 array 생성
print(a)
b = np.ones((1,2)) # 모든 값이 1인 1x2 array 생성
print(b)
c = np.full((2,2), 7) # 모든 값이 7인 2x2 array 생성
print(c)
d = np.eye(2) # 2x2 단위행렬(Identity matrix) 생성
print(d)
e = np.random.random((2,2)) # 0~1 랜덤 값을 가지는 2x2 array 생성
print(e)
```

