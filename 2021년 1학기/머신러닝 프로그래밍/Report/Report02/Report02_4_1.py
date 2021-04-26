from sklearn.linear_model import Perceptron  #퍼셉트론 함수 사용 준비

#훈련 집합 구축
X = [ [0,0], [0,1], [1,0], [1,1] ]

#Or Gate Result
y_OR = [-1, 1, 1, 1]

#AND Gate Result
y_AND = [-1, -1, -1, 1]

#NAND Gate Result
y_NAND = [1, -1, -1, -1]

#XOR Gate Result
y_XOR = [-1, 1, 1, -1]

dataSet = [] #각 Gate 이름, y값, 퍼셉트론 객체를 관리하기 위한 변수

# fit 함수로 OR Gate Perceptron 학습
p_OR = Perceptron()
p_OR.fit(X, y_OR)
dataSet.append(["[OR Gate Result]", y_OR, p_OR])

# fit 함수로 AND Gate Perceptron 학습
p_AND = Perceptron()
p_AND.fit(X, y_AND)
dataSet.append(["[AND Gate Result]", y_AND, p_AND])

# fit 함수로 NAND Gate Perceptron 학습
p_NAND = Perceptron()
p_NAND.fit(X, y_NAND)
dataSet.append(["[NAND Gate Result]", y_NAND, p_NAND])

# fit 함수로 XOR Gate Perceptron 학습. XOR의 경우 다층 퍼셉트론을 사용해야하나 오동작 확인을 위해 추가
p_XOR = Perceptron()
p_XOR.fit(X, y_XOR)
dataSet.append(["[XOR Gate Result]", y_XOR, p_XOR])

for i in range(0, len(dataSet)):
    print(dataSet[i][0])
    print("  학습된 퍼셉트론의 매개변수: ", dataSet[i][2].coef_, dataSet[i][2].intercept_)
    print("  훈련 집합에 대한 예측: ", dataSet[i][2].predict(X))
    print("  정확률 측정: ", dataSet[i][2].score(X, dataSet[i][1]) * 100, "%")
