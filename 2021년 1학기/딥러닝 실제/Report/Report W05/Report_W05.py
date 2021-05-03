import numpy as np

def AND(x1, x2):
    x = np.array([x1, x2])
    w = np.array([0.5, 0.5])
    b = -0.7
    tmp = np.sum(w * x) + b

    if tmp <= 0:
        return 0
    else:
        return 1

def NAND(x1, x2):
    x = np.array([x1, x2])
    w = np.array([-0.5, -0.5])
    b = 0.7
    tmp = np.sum(w * x) + b

    if tmp <= 0:
        return 0
    else:
        return 1

def OR(x1, x2):
    x = np.array([x1, x2])
    w = np.array([0.5, 0.5])
    b = -0.2
    tmp = np.sum(w * x) + b

    if tmp <= 0:
        return 0
    else:
        return 1

def XOR(x1, x2):
    s1 = NAND(x1, x2)
    s2 = OR(x1, x2)
    return AND(s1, s2)

def FullAdder(x, y, z):
    firstLayerXOR = XOR(x, y)
    firstLayerAND = AND(x, y)

    secondLayerXOR = XOR(firstLayerXOR, z)
    secondLayerAND = AND(z, firstLayerXOR)

    thirdLayerOR = OR(secondLayerAND, firstLayerAND)

    s = secondLayerXOR
    c = thirdLayerOR

    return s, c

def exitByOutOfRange():
    print('0과 1만 입력 가능합니다. 강제 종료합니다')
    exit(0)

def checkRangeOfValue(data):
    if data > 1 or data < 0:
        exitByOutOfRange()

x = int( input ('x를 입력하시오 :'))
checkRangeOfValue(x)

y = int( input ('y를 입력하시오 :'))
checkRangeOfValue(y)

z = int( input ('z를 입력하시오 :'))
checkRangeOfValue(z)

sum, carry = FullAdder(x, y, z)
print('Sum=',sum, ' Carry=',carry)