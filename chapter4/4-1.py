# 함수


# 기본 구조
# 입력 o 리턴 o
'''
def add(a, b): # a, b는 매개변수, 파라미터, 인자
    result = a + b
    return result

print(add(1, 2)) # 1, 2는 인수 # 3
'''

# 입력 x 리턴 o
'''
def say():
    return 'Hi'

print(say()) # Hi
'''

# 입력 o 리턴 x
'''
def minus(a, b):
    print(f'{a} 빼기 {b}는 {a-b}입니다.')

print(minus(1, 5)) # 1 빼기 5는 -4입니다. None
'''
# return이 없기 때문에 minus함수 결과에 None이 저장됨.
# print값은 retrun이 아니라 minus함수 중간에 실행된것일 뿐

# 입력 x 리턴 x
'''
def say2():
    print('Hi')

print(say2()) # Hi None
'''

# 입력값이 몇 개가 될 지 모를 때 # *args
'''
def add_many(*args):
    result = 0
    for i in args:
        result = result + i
    return result

print(add_many(1, 2, 3, 4, 5))
'''

# 그냥 매개변수랑 *args랑 섞어쓰기
'''
def add_mul(choice, *args):
    if choice == 'add':
        result = 0
        for i in args:
            result += i
    if choice == 'mul':
        result = 1
        for i in args:
            result = result * i
    return result

c = add_mul('mul', 1, 2, 3, 4, 5)
print(c)
'''

# **kwargs(keyword args) # 딕셔너리 형태로 받게 됨
'''
def print_kwargs(**kwargs):
    print(kwargs)

print_kwargs(a = 1, b = 2) # {'a': 1, 'b': 1}
'''

# 활용법 # 여러개의 값 중에서 원하는 것만 추출
'''
def print_kwargs(**kwargs):
    print(kwargs['a'])
    print(kwargs['b'])

print_kwargs(a = 1, b = 2) # {'a': 1, 'b': 1}
'''

# 함수의 리턴값은 언제나 하나
'''
def add_and_mul(a, b):
    return a + b, a * b

print(add_and_mul(4, 5)) # (9, 20) # 두개의 값을 리턴 요청했지만 나오는 리턴값은 튜플 하나

# return 두개 연속 하면 첫번째 리턴만 인식됨
# 즉 return문을 만나면 함수를 빠져나가게 되는 거임

# 그래서 이렇게도 쓸 수 있다
def say_nick(nick):
    if nick == '바보':
        return # 함수를 빠져나가는 기능으로 사용한 return
    print(f'나의 별명은 {nick} 입니다')

nick = str(input('당신의 별명을 입력하세요 : '))
print(say_nick(nick))
'''

# 매개변수 초깃값 미리 설정해두기
'''
def introduce_muself(name, age, man = True): # 기본값이 설정된 매개변수는 항상 맨 뒤에 써야 한다
    print(f'내 이름은 {name}입니다.')
    print(f'나이는 {age}살 입니다.')
    if man:
        print('남자입니다.')
    else:
        print('여자입니다.')

Lim_Taek = introduce_muself('임택', 20)
# 남자를 기본값으로 할 수 있고, 여자면 False를 추가하는 식
# 참고로 인자 순서는 등호로 지정하지 않는 이상 매개변수 설정값 순서로 써야한다
print(Lim_Taek)
'''

# 함수 안에서 함수 밖의 변수를 변경하는 방법
# 1. return
'''
a = 1
def vartest(a):
    a += 1
    return a
a = vartest(a)
print(a)
'''

# 2. global
'''
a = 1
def vartest():
    global a
    a += 1

vartest()
print(a)
# 함수 밖의 a 변수를 직접 사용하겠다는 뜻이다.
# 하지만 사용하지 않는 것이 좋다. 함수는 독립적으로 존재하는 것이 좋기 때문
'''

# mutable immutable
'''
a = 1
def vartest(a):
    a = a + 1
    return a

print(vartest(a)) # 2
print(a) # 1
# immutable 자료형이기에 함수 밖에서는 영향을 받지 않는 모습
'''
'''
b = [1, 2, 3]
def vartest2(b):
    b = b.append(4) # 지역변수 b에는 append이기에 None이 대입되고 append함수로 mutable자료형인 list에 영향을 준다

vartest2(b)
print(b)
# mutable 자료형이라 함수 밖에서도 영향을 받음
'''

# lambda 예약어
'''
# 함수_이름 = lambda 매개변수1, 매개변수2, ... : 매개변수를_이용한_표현식
# 이름을 지어도 되고, 안지어도 된다

add = lambda a, b: a+b
print(add(2, 3)) #변수에 할당해서 사용

print((lambda a, b: a*b)(1, 2)) #바로 사용
'''
