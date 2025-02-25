# 1
'''
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def greet(self):
        print(f'{self.name}님이 {self.age}살입니다.')

p1 = Person('임택', 20)
print(p1.greet())
'''

# 2
'''
class BankAccount:
    def __init__(self, account_number, balance = 0):
        self.account_number = account_number
        self.balance = balance
    def deposit(self, amount):
        self.balance += amount
    def withdraw(self, amount):
        if self.balance < amount:
            print('잔액이 부족합니다.')
            return #return으로 잔액이 부족하면 그냥 함수 종료시켜서 돈 차감 안되게 함
        self.balance -= amount
    def ShowMyBalance(self):
        print(self.balance)

acc1 = BankAccount(12345, 1000)
acc1.ShowMyBalance()
acc1.deposit(2000)
acc1.ShowMyBalance()
acc1.withdraw(4000)
acc1.withdraw(200)
acc1.ShowMyBalance()
acc1.withdraw(4000)
acc1.ShowMyBalance()
'''

# 3
'''
import caculator_practice_mod

print(caculator_practice_mod.add(3, 4))
print(caculator_practice_mod.sub(3, 4))
print(caculator_practice_mod.div(3, 0))
'''

# 4
'''
import random

a = []

for i in range(1, 11):
    a.append(random.randrange(1, 101))

a.sort() #sort는 a리스트 자체를 바꿈. 리턴값은 None이다

print(a)
'''
'''
import random

random_numbers = [random.randint(1, 100) for i in range(10)]
sorted_numbers = sorted(random_numbers)
#sorted는 정렬된 값을 리턴함. 본래의 리스트는 변하지 않는다
print("오름차순 정렬:", sorted_numbers)
'''

# 5
'''
from my_math.operations import add, sub

print(add(3, 4))
print(sub(3, 4))
'''

# 6
'''
from my_math.geometry import circle_area, rectangle_area

print(circle_area(2))
print(rectangle_area(3, 4))
'''

# 7
'''
try:
    number = input('숫자를 입력하세요 : ')
    squared_number = int(number) ** 2
    print(f'입력한 숫자의 제곱 : {squared_number}')
except ValueError:
    print('숫자를 입력해야 합니다.')
'''

# 8
'''
numerator = 10
denominator = 0

try:
    result = numerator / denominator
    print(f'결과 : {result}')
except ZeroDivisionError:
    print('0으로 나눌 수 없습니다.')
'''

# 9
'''
numbers = [3, 7, 2, 1, 6, 4, 9, 8]

max_value = max(numbers)
min_value = min(numbers)

print(f'최댓값 : {max_value}')
print(f'최솟값 : {min_value}')
'''

# 10
'''
text = "hello world, this is a python example."

splited_text = text.split()
capitalized_splited_text = [i.capitalize() for i in splited_text]
result = ' '.join(capitalized_splited_text)
print(result)
'''

# 11
'''
import datetime

current_time = datetime.datetime.now()
print(f'현재 날짜와 시간 : {current_time}')
'''

# 12
'''
import random

l1 = [random.randint(1, 100) for i in range(1, 11)]
result = ' '.join(map(str, l1)) #join은 문자열 리스트만 받을 수 있기에 map함수로 str으로 바꿀거임
print(result)
'''
