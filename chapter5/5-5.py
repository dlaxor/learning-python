### 내장 함수

## abs # absolute value
# 그 수의 절댓값을 리턴한다
a = abs(-2)
#print(a)


## all
# 요소가 모두 참이면 True, 하나라도 거짓이면 False
b = all([1, 0, 2]) # 근데 비어있으면 True
#print(b)


## divmod
# divmod(a, b)면 a를 b로 나눴을 때 몫과 나머지를 튜플로 리턴한다.
c = divmod(5,3)
#print(c)


## enumerate
# 순서가 있는 데이터(리스트, 튜플, 문자열, 딕셔너리)를 입력으로 받아 인덱스 값을 포함하는 enumerate 객체를 리턴한다.
# 보통 for문과 함께 사용한다
#for i, name in enumerate(['body', 'foo', 'bar']):
#    print(i, name)


## eval
# eval(expression)은 문자열로 구성된 표현식을 입력으로 받아 해당 문자열을 실행한 결괏값을 리턴하는 함수이다.
'''
while True:
  exp = input('표현식 : ')
  if exp == 'exit':
    break
  
  result = eval(exp)
  print(result)
'''


## filter
# filter 함수는 첫 번째 인수로 함수, 두 번째 인수로 그 함수에 차례로 들어갈 반복 가능한 데이터
# 반복 가능한 데이터의 요소 순서대로 함수를 호출했을 때 리턴값이 참인 것만 묶어서(걸러 내서) 리턴한다.
'''
def positive(x):
    return x > 0

print(list(filter(positive, [1, -3, 2, 0, -5, 6])))
'''


## id
# 객체를 입력받아 객체의 고유 주솟값(레퍼런스)을 리턴하는 함수이다.
d = 3
#print(id(3))


## int
# 숫자나 소수점이 있는 숫자를 정수로 리턴하는 함수
pi = 3.141592
#print(int(pi))


## isinstance
# 첫 번째 인수로 객체, 두 번째 인수로 클래스
# 입력으로 받은 객체가 그 클래스의 인스턴스인지를 판단
class Person:
    pass

e = Person()
print(isinstance(a, Person))


## len
# 길이
f = 'what have we done'
#print(len(f))


## map
# map(f, iterable)은 함수(f)와 반복 가능한 데이터를 입력으로 받는다.
# 입력받은 데이터의 각 요소에 함수 f를 적용한 결과를 리턴
def two_times(x): 
    return x*2
    
#print(list(map(two_times, [1, 2, 3, 4])))


## max, min
g = max([1, 2, 3])
h = min("python")
#print(g, h)


## pow
# pow(a, b) # a**b 리턴


## range
# 3번째 인수는 간격
i = list(range(1, 10, 2))
print(i)


## round
# 숫자를 입력받아 반올림해 리턴하는 함수이다.
j = round(4.5)
#print(j)
k = round(4.6425, 2)
#print(k)


## sum
l = [1, 2, 3]
#print(sum(l))


## zip
names = ["Alice", "Bob", "Charlie"]
ages = [25, 30, 35]
zipped = zip(names, ages)
#print(list(zipped))