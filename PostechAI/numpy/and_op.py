import numpy as np

x1 = np.array([0,0])
x2 = np.array([0,1])
x3 = np.array([1,0])
x4 = np.array([1,1])

W = np.array([[1,1],
              [3,6]])
b = np.array([6,0])

print(np.argmax(W.dot(x1)+b))
print(np.argmax(W.dot(x2)+b))
print(np.argmax(W.dot(x3)+b))
print(np.argmax(W.dot(x4)+b))
