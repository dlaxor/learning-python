# 변수

# 변수란 객체를 가리키는 것이라고 할 수 있다.
# 객체란 자료형의 데이터(값)을 의미함
'''
a = [1, 2, 3]
# [1, 2, 3]은 객체(리스트 데이터), 객체가 저장된 메모리의 주소는 변수 a
print(id(a)) # 2692272716864 (주소)

b = a #b도 a가 가리키는 리스트를 가리키게 하겠다
print(id(a))
print(id(b)) #똑같게 나온다

print(a is b) #a와 b는 같은 객체를 가리키니?
#True

a[0] = 4 #a가 가리키는 리스트를 바꿈 => b도 가리키므로 바뀜
print(a) # [4, 2, 3]
print(b) # [4, 2, 3]
print(id(a)) 
print(id(b)) # 같은 값
'''

#그럼 같은 리스트 값을 가졌는데 주소는 다르게 할 수는 없나?
# 1. [:] 이용하기
'''
a = [1, 2, 3]
b = a[:]
print(a) # [1, 2, 3]
print(b) # [1, 2, 3]
print(id(a))
print(id(b)) # 다른 값
'''
# 2. copy 모듈 이용하기
'''
from copy import copy
c = copy(a)
print(c) # [1, 2, 3]
print(a is c) # False # 다른 값
'''
# 3. copy 함수 이용하기
'''
d = a.copy()
print(d is a) # False
'''

# 변수를 생성하는 다양한 방법들
# a = 'python'
# b  = 3

# 튜플로 생성하는법
'''
a, b = ('python', 3)
a, b = 'python', 3
(a, b) = ('python', 3)
(a, b) = 'python', 3
print(a, b) # python 3
'''
# 여러 개의 변수에 같은 값 대입 가능
'''
a = b = 'python'
print(a)
print(b) #둘 다 python
'''
# 두 변수의 값을 바꾸는법
a = 3
b = 5
a , b = b , a
print(a) # 5
print(b) # 3