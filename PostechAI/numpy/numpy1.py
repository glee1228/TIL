import numpy as np

a = np.array([1,2,3]) # 1차원 array [1,2,3] 생성

# 값을 직접 입력해서 생성하는 방법
print(type(a))
print(a.shape)
print(a[0], a[1], a[2])
a[0] = 5
print(a)
b = np.array([[1,2,3],[4,5,6]])
print(b.shape)
print(b[0, 0], b[0, 1], b[1, 0])

# 값을 직접 주지않고 생성하는 방법
print("----------------------------------")
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
print("-------------------------------")
#Array Slicing

a = np.array([[1,2,3,4],[5,6,7,8],[9,10,11,12]])
# 첫번째 행의 처음부터 2 앞까지(0,1), 두번째 행에서
# 1부터 3 앞까지(1,2)의 값들을 떠와 b에 할당.
# 따라서 b 는 다음과 같은 2x2 array:
# [[2 3]
# [6 7]]
b = a[:2, 1:3]
c = a[1:3,1:3]
d = a[1:3,1:]
print(d)
print(c)
print(a)
print(b)
print(a[0, 1])
b[0, 0] = 77
print(b)
print(a[0, 1])
# Slicing을 한다고 해서 값을 복사해가는 것이 아니므로
# 값의 변화가 동시에 일어남

print("-------------------------------")
# 2차원 배열(3x4) 생성
# [[ 1 2 3 4]
# [ 5 6 7 8]
# [ 9 10 11 12]]
a = np.array([[1,2,3,4],[5,6,7,8],[9,10,11,12]])
# 두 번째 행의 값들을 모두 가져오는 두 가지 방법
row_r1 = a[1, :] # 1차원 행렬 (4,)
row_r2 = a[1:2, :] # 2차원 행렬 (1x4) – 기존 차원 유지
print(row_r1, row_r1.shape)
print(row_r2, row_r2.shape)
# 두 번째 열의 값들을 모두 가져오는 두 가지 방법
col_r1 = a[:, 1]
col_r2 = a[:, 1:2]
print(col_r1, col_r1.shape)
print(col_r2, col_r2.shape)
print(globals())