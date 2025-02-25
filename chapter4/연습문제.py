# 1
# 주어진 문자열을 반대로 뒤집는 함수
'''
def reverse(a):
    return a[::-1]

input_str = str(input('뒤집을 문자열을 입력하세요 : '))
output_str = reverse(input_str)
print(output_str)
'''

# 2
# 소수를 판별하는 함수 작성하기
'''
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, n):
        if n % i == 0: # 2부터 n-1까지 나눠서 한번이라도 나머지가 0인지 확인
            return False # 반복문을 다 돌고
    return True # 통과하면 그제서야 True

num = int(input('소수인지 판별할 수를 입력하세요 : '))
result = is_prime(num)
print(result)
'''

# 3
'''
num = int(input('제곱할 숫자를 입력하세요 : '))
print(num*num)
'''
'''
num = float(input())
square = num**2
print(f'입력한 수의 제곱 : {square}')
'''

# 4
'''
name = str(input('이름을 입력하세요 : '))
age = int(input('나이를 입력하세요 : '))

age_10y_later = age + 10
print(f'{name}님의 10년 후 나이는 {age_10y_later} 입니다.')
'''

# 5
# 사용자로부터 입력받은 내용을 파일에 작성하기
'''
input = input('추가할 내용을 입력하세요 : ')

f = open('input.txt', 'w', encoding='utf-8')
f.write(input)
f.close
'''
'''
input = input('추가할 내용을 입력하세요 : ')
with open('input.txt', 'w', encoding='utf-8') as f:
    f.write(input)

print('입력한 내용이 input.txt에 저장되었습니다.')
'''

# 6
# 파일의 모든 줄을 읽어 대문자로 변환하여 출력하기
'''
f = open('example.txt', 'w', encoding='utf-8')
f.write('apple banana kiwi sandwich ameba')
'''
'''
f = open('example.txt', 'r', encoding='utf-8')
input = f.read()
output = input.upper()
print(output)
'''
'''
with open('example.txt', 'r', encoding='utf-8') as f:
    for line in f:
        print(line.upper().strip()) # strip은 줄바꿈문자 지우기용
print("example.txt 파일의 내용을 대문자로 출력하였습니다.")
'''

# 7
# 명령 줄 인수를 사용하여 두 숫자의 사칙연산 결과 출력하기

import sys

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    return a / b

num1 = float(sys.argv[1])
operator = sys.argv[2]
num2 = float(sys.argv[3])

if len(sys.argv) > 4:
    print('사용법 : 숫자1, 연산자, 숫자2')

if operator == '+':
    result = add(num1, num2)
if operator == '-':
    result = subtract(num1, num2)
if operator == '*':
    result = multiply(num1, num2)
if operator == '/':
    result = divide(num1, num2)

print(result)