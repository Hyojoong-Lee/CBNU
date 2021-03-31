import numpy as np
import matplotlib.pylab as plt


def step_function1(x):
    if x > 0:
        return 1
    else:
        return 0

def step_function2(x):
    y = x > 0
    return y.astype(np.int)

'''
x = np.array( [-1.0, 1.0, 2.0])
print(x)
y = x > 0
print(y)
y= y.astype(np.int)
print(y)
'''

def step_function3(x):
    return np.array(x > 0, dtype = np.int)
'''
x = np.arange(-5.0, 5.0, 0.1)
y = step_function3(x)
plt.plot(x,y)
plt.ylim(-0.1, 1.1)
plt.show()
'''
def sigmoid(x):
    return (1/(1+np.exp(-x)))
'''
x = np.arange(-5.0, 5.0, 0.1)
y = sigmoid(x)
plt.plot(x,y)
plt.ylim(-0.1, 1.1)
plt.show()
'''
def ReLU(x):
    return (np.maximum(0, x)) #np.maximum(x,y)는 둘 중 큰값을 리턴
'''
x = np.arange(-5.0, 5.0, 0.1)
y = ReLU(x)
plt.plot(x,y)
plt.ylim(-0.1, 1.1)
plt.show()
'''

#Array
'''
A = np.array([1,2,3,4])
print(A)
print(np.ndim(A))
print(A.shape)
print(A.shape[0])
'''
# Matrix
'''
B = np.array( [[1,2], [3,4], [5,6]])
print(B)
print(np.ndim(B))
print(B.shape)
print(B.shape[0])
'''
#행렬의 곱셈
'''
C = np.array( [[1,2], [3,4]])
D = np.array( [[5,6], [7,8]])
if C.shape[1] == D.shape[0]:#행렬의 곰셉이 가능한지 확인
    print(np.dot(C,D))
'''
'''
A = np.array( [[1,2], [3,4],[5,6]])
#B = np.array( [7,8]) #아래와 둘다 가능. 얘는 1x3 출력
B = np.array( [[7],[8]]) #얘는 3x1로 출력
if A.shape[1] == B.shape[0]:#행렬의 곰셉이 가능한지 확인
    print(np.dot(A,B))
'''

'''
X = np.array( [1,2])
print(X.shape)
W = np.array( [[1,3, 5], [2,4, 6]])
print(W)
print(W.shape)
if X.shape[0] == W.shape[0] or X.shape[1] == W.shape[0]:#행렬의 곰셉이 가능한지 확인
    print(np.dot(X,W))
else:
    print('Not Match')
'''

X = np.array( [1.0, 0.5])
W1 = np.array( [ [0.1, 0.3, 0.5], [0.2, 0.4, 0.6]])
B1 = np.array( [1.0, 0.2, 0.3])
print(W1.shape)
print(X.shape)
print(B1.shape)
A1 = np.dot(X,W1) + B1
print(A1)