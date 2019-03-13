"""
선형 연립방정식 풀이 방법 요약(공부가 필요한 부분)
Ax = B 형태
1. A의 역행렬이 존재하는 경우 : X= A^(-1)B
2. A의 역행렬이 존재하지 않는 경우 : X = A^(+)B (단, A^(+)는 pseudo inverse)

Ax = 0 형태
1. A의 특이값분해(SVD)를 A = U\sigmaV^T 라 할 때,
X는 V의 가장 오른쪽 열벡터(즉, A의 최소특이값에 대응하는 right singular vector)

NumPy의 linalg 서브패키지에는 역행렬을 구하는 inv 라는 명령어가 존재한다.
Ax = b -> x = A역행렬 * b
선형 연립방정식의 행렬 A 의 역행렬은 np.linalg.inv()함수로 구할 수 있다.
하지만, 정방행렬이 아니므로 역행렬을 구할 수 없다.
이 경우엔, A의 의사역행렬을 이용하여 X를 근사적으로 구한다.
A^(+) = (A^TA)^(-1)A^T

하지만, 이 문제는 np.linalg.lstsq()함수로 간단하게 풀 수 있다.

"""

import numpy as np

A = np.array([[1,1,0],[0,1,1],[1,1,1],[1,1,2]])
b = np.array([[2],[2],[3],[4.1]])

x, resid, rank, s = np.linalg.lstsq(A,b)
X = x.T

print('최소자승법의 해의 전치행렬 :',X)


#print('최소자승법의 해 : ',x)
#print('잔차제곱합(residual sum of square): ',resid)
#print('랭크 :',rank)
#print('특이값(singular value :',s)

#X = [x1,x2,x3]의 전치행렬(transpose matrix)
