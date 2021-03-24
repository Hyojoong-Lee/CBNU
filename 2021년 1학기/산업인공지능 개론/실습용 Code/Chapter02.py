'''
sum = 0
for x in range(1, 10, 2):
  sum += x
print(sum)
'''

'''
sum = 0
limit = int(input("What is the limit :"))
for i in range(1, limit+1):
    sum += i
    
print("The sum (from 1", "to ", limit,") is ", sum)
'''

'''
i = 0 
while i < 10:
    print(i, end=" ")
    i+=1
print("End the loop")
'''

'''
i = 0 
while i < 10:
    print(i, end=" ");
    i+=1
print("End the loop", i)
'''

'''
i=1
sum = 0

while i <= 10:
  sum += i
  i += 1
print(sum)
'''

'''
i=1
factorial = 1

while i <= 10:
  factorial *= i
  i += 1
print("10! is %d"%factorial)
'''

'''
nDan = int(input("몇단 ? : "))
i = 1
while i <= 9:
    result = nDan * i
    print("%d * %d = %d"%(nDan, i, result))
    i += 1
'''

'''
sum = 0
n = int(input("몇의 배수 : "))
limit = int(input("몇 까지 : "))
number = 1
while number <= limit:
    if number % n == 0:
        sum += number
    number += 1
    
print("1부터 %d까지 %d의 배수들의 합은 %d"%(limit, n, sum))
'''

'''
def get_sum(start, end):
    sum = 0 
    for i in range(start, end+1):
        sum += i
    return sum

value = get_sum(1,10)
print(value)
'''

'''
def FtoC(temp_f):
    temp_c = (5.0 * (temp_f - 32.0)) / 9.0
    return temp_c

print(FtoC(float(input("화씨 온도를 입력하시오 : "))))
'''


