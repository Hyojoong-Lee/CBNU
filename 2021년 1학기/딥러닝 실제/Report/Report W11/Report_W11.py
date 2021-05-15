# -*- coding: utf-8 -*-
"""
Created on Tue May 11 19:42:33 2021

@author: kircheis
"""

from sklearn.datasets import fetch_openml
from sklearn.neural_network import MLPClassifier
import matplotlib.pyplot as plt
import numpy as np
import time

# MNIST 데이터셋을 읽고 훈련 집합과 테스트 집합으로 분할
start = time.time()
mnist=fetch_openml('mnist_784')
mnist.data=mnist.data/255.0
x_train=mnist.data[:60000]
x_test=mnist.data[60000:]
y_train=np.int16(mnist.target[:60000])
y_test=np.int16(mnist.target[60000:])
end = time.time()
print("Data Set loading 소요 시간 :", end-start)

# MLP 분류기 모델을 학습
start = time.time()
mlp=MLPClassifier(hidden_layer_sizes=(100),learning_rate_init=0.001,batch_size=128,max_iter=300,solver='adam',verbose=True)
mlp.fit(x_train,y_train)
end = time.time()
print("학습 소요 시간 :", end-start)


# 테스트 집합으로 예측
res=mlp.predict(x_test)


# 혼동 행렬
conf=np.zeros((10,10),dtype=np.int16)
for i in range(len(res)):
    conf[res[i]][y_test[i]]+=1
print(conf)

# 정확률 계산
no_correct=0
for i in range(10):
    no_correct+=conf[i][i]
accuracy=no_correct/len(res)
print("테스트 집합에 대한 정확률은", accuracy*100, "%입니다.")