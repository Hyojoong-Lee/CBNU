
def perceptron_StepFunc(x1, x2, weight1, weight2, bias):
    outX1 = x1 * weight1
    outX2 = x2 * weight2
    result = outX1 + outX2 + bias
    if result >= 0:
        return True
    return False

def OR_Gate(x1, x2):
    return perceptron_StepFunc(x1, x2, 1, 1, -0.5)

def AND_Gate(x1, x2):
    return perceptron_StepFunc(x1, x2, 1, 1, -1.5)

def NAND_Gate(x1, x2):
    return perceptron_StepFunc(x1, x2, -1, -1, 1.5)

def XOR_Gate(x1, x2):
    resultNAND = NAND_Gate(x1, x2)
    resultOR = OR_Gate(x1, x2)
    return AND_Gate(resultNAND, resultOR)

def exitByOutOfRange():
    print('0과 1만 입력 가능합니다. 강제 종료합니다')
    exit(0)

def checkRangeOfValue(data):
    if data != 1 and data != 0:
        exitByOutOfRange()

x1 = int(input('x1 :'))
checkRangeOfValue(x1)
x2 = int(input('x2 :'))
checkRangeOfValue(x2)

print('OR gate result =', OR_Gate(x1,x2))
print('AND gate result =', AND_Gate(x1,x2))
print('NAND gate result =', NAND_Gate(x1,x2))
print('XOR gate result =', XOR_Gate(x1,x2))