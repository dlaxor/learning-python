# 1
'''
print('정수를 입력하시오')
a = int(input())

if a % 2 == 0:
    print('짝수입니다.')
else:
    print('홀수입니다.')
'''

# 2
# 사용자로부터 세 개의 정수를 입력받고, 가장 큰 수를 출력
'''
a = int(input("첫 번째 정수를 입력하세요 : "))
b = int(input("두 번째 정수를 입력하세요 : "))
c = int(input("세 번째 정수를 입력하세요 : "))

if a >= b and a >= c:
    max = a
elif b >= a and b >= c:
    max = b
elif c >= a and c >= b:
    max = c

print(f'가장 큰 수는 {max}입니다.')
'''

# 3
# 1부터 사용자가 입력한 숫자까지의 합

# my answer (for)
'''
add = 0
a = int(input("정수를 입력하세요 : "))
for i in range(1, a+1):
    add = add + i
print(add)
'''

# book's answer (while)
'''
user_input = int(input("숫자를 입력하세요: "))
sum = 0
i = 1
while i <= user_input:
    sum = sum + i
    i = i + 1
print(sum)
'''

# 4
# 피보나치 수열의 n번째 항까지 출력
'''
a = 1
b = 1
i = 1
n = int(input())
while i <= n:
    print(a)
    a, b = b, a + b
    i = i + 1
'''

# 5
# 구구단
'''
for i in range(2, 10):
    print(f'{i}단 : ', end = '')
    for j in range(1, 10):
        print(i * j, end = ' ')
    print('')
'''

# 6
# 주어진 문자열에서 모음(a, e, i, o, u)의 개수를 세기
'''
text = "The quick brown fox jumps over the lazy dog"
vowels = 'aeiou'
count = 0

for i in text.lower():
    if i in vowels:
        count += 1
print(f'주어진 문자열에는 모음이 {count}개 있습니다.')
'''