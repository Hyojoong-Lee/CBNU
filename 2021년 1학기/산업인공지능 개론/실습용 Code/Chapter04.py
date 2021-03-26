# 2021 03 25 산업인공지능 개론

# tuple 실습
# tuple은 선언할 때 배열을 소괄호로 Block. 소괄호 없어도 된다.
#t = (0,1,2)
# tuple은 변경이 불가능하다
#t[0] = 100 #error
# 하나의 값을 갖는 tuple은 반드시 값 다음에 쉼표 필요
#t2 = (0,)

'''
# tuple의 중첩
t3 = (1,2, 'hello')
u = t3,(1,2,3,4)
print(u)
'''

'''
#원면적과 둘레 계산 : P12
import math
def calCircle(r):
    area = math.pi *r *r
    circum = 2 * math.pi * r
    return (area, circum)

radius = float( input("Enter thr R: "))
(a,c) = calCircle(radius)
print('area ='+str(a), 'and length ='+str(c))
'''


# 세트(Set, 집합) : 중괄호로 Block. 즉, List는 대괄호, Set는 중괄호, tuple은 소괄호 혹은 없음
# - 집합을 나타내는 자료구조
# - 중복되지 않는 항목들이 모인 것
# - 항목간에는 순서가 없음
# 연산자 < 는 부분 집합인지 확인
# sub set은 부분 집합
# union 은 합집합
# inter section 는 교집합
'''
numbers = { 11,  5, 10, 1}
for x in numbers:
    print(x, end=' ')
'''
'''
numbers = {2,1,3}
print(numbers)
print(len(numbers))
'''

# 딕셔너리
# 키와 값을 쌍으로 저장할 수 있는 객체. set에 인덱스를 위한 키가 추가된거로 보면 될듯
# dic = { 키1:값1, 키2:값2...}
# 키값으로 각 Data에 접근
'''
scores = { 'Korean': 80, 'Math': 90, 'English': 80}
for item in scores.items():
    print(item)
'''
'''
triples = { x: x*x*x for x in range(6)}
print(triples)
'''
'''
dic= {"bags":1, "coins":7, "bottles":4, "books":5}
A = list(dic)
sortKeys= sorted(dic)
sortedValues= sorted(dic.values())
print(sortKeys)
print(sortedValues)
'''
'''
english_dict= dict()
english_dict['one'] = '하나'
english_dict['two'] = '둘'
english_dict['three'] = '셋'
word = input("Enter the ward: ");
print (english_dict.get(word, "Not existing"))
'''

# 문자열
'''
word = 'Python'
print(word[0:2])
print(word[2:5])
'''