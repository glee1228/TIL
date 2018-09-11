import numpy as np
a= np.array([[1,2,3,4],[5,6,7,8],[9,10,11,12]])

row_r1 = a[1, :] # 1차원 행렬 (4,)
row_r2 = a[1:2, :] # 2차원 행렬 (1x4) – 기존 차원 유지
print(row_r1, row_r1.shape)
print(row_r2, row_r2.shape)
# 두 번째 열의 값들을 모두 가져오는 두 가지 방법
col_r1 = a[:, 1]
col_r2 = a[:, 1:2]
print(col_r1, col_r1.shape)
print(col_r2, col_r2.shape)
print(np.array([0,0]))
print(np.array([0,1]))
print(np.array([1,0]))
print(np.array([1,1]))


"""
x = np.array([[1, 2],
              [3, 4]])
y = np.array([[5, 6],
              [7, 8]])
v = np.array([9, 10])
w = np.array([11, 12])
# v · w = 219 print v.dot(w) print np.dot(v, w)
# 매트릭스 / 벡터 곱;[2967] print x.dot(v)
print(x)
print(v)
print(np.dot(x, v))
# 매트릭스 / 매트릭스 곱; # [[19 22]
# [43 50]]
print(x.dot(y))
print(np.dot(x, y))
"""