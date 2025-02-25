#불 자료형 #불 자료형이란 True와 False를 나타내는 자료형이다.
#True나 False는 파이썬의 예약어
#true, false와 같이 작성하면 안 되고 첫 문자를 항상 대문자로 작성해야 한다.
'''
a = False
print(type(a)) # <class 'bool'>
'''

# ==은 두 값이 같은지 비교하여 True 혹은 False를 반환
# 따라서 ==의 연산 결과는 항상 불 자료형
'''
a = 1
b = 1
c = 2
print(a == b) # True
print(a == c) # False
print(a < b) # False
print(a <= b) # True
'''
a = bool([])
print(a) # False # 리스트 안이 비어있기 때문에 False값
