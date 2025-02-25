# if 문

'''
money = True

if money:
    print("택시를 타고 가라")
else:
    print("걸어 가라") 
# 만약에 money가 True면 "택시를 타고 가라"를 출력하고,
# False면 "걸어 가라" 를 출력해라
'''

'''
score = 100

if score >= 60: # 스코어가 60이상인게 True면
    message = "success" # message 변수에 success 문자열 대입
else:
    message = "failure"

print(message)
''' #message는 조건문을 통해 값이 할당되는 변수이기에 초기값 필요 x

# 비교연산자
'''
x = 3
y = 2
print(x > y) # True
print(x <= y) # False
print(x != y) #True
print(x == y) # False
'''

# 만약 3000원 이상의 돈을 가지고 있으면 택시를 타고 가고, 그렇지 않으면 걸어가라.
'''
current_money = 2000
if current_money >= 3000:
    print("택시를 타고 가라")
else:
    print("걸어가라")
'''

# 조건 판단 연산자
# 1) x or y - x와 y중 하나만 참이어도 참
# 2) x and y - x와 y 모두 참이면 참
# 3) not x - x가 거짓이면 참
# 4) x in 리스트,튜플,문자열 / not in - 포함되면 참

# or 사용 예시
'''
money = 2000
card = True
if money >= 3000 or card: # 돈이 3000원 이상인게 True거나 card가 True면
    print("택시를 타고 가라") # "택시를 타고 가라" 를 print해라
else:
    print("걸어가라")
# 돈이 부족해도 카드가 있기에 택시를 탈 수 있다
'''

# in 사용 예시
'''
print(1 in [1, 2, 3]) #True
print('a' not in 'apple') #False
'''

'''
pocket = ['paper', 'cellphone', 'money']
if 'money' in pocket:
    print("택시를 타고 가라")
else:
    pass # 아무것도 하지 않고 싶을 때는 pass를 쓰면 됨
'''

#elif의 장점
#주머니에 돈이 있으면 택시를 타고 가고,
#주머니에 돈은 없지만 카드가 있으면 택시를 타고 가고, 돈도 없고 카드도 없으면 걸어가라.

#elif를 사용하지 않았을 때
'''
pocket = ['paper', 'cellphone', 'money']
card = True
'''

'''

if 'paper' in pocket:
    print("택시 ㄱㄱ")
else:
    if card:
        print("택시 ㄱㄱ")
    else:
        ("걸어라")
'''

#elif를 사용했을때
'''
if 'paper' in pocket:
    print("택시 ㄱㄱ")
elif card:
    print("택시 ㄱㄱ")
else:
    print("걸어라")
'''

#elif문 구조
'''
if 조건문:
    수행할_문장1 
    수행할_문장2
    ...
elif 조건문:
    수행할_문장1
    수행할_문장2
    ...
elif 조건문:
    수행할_문장1
    수행할_문장2
    ...
...
else:
   수행할_문장1
   수행할_문장2
   ... 
'''

'''
a = "python" # 문자열이 채워져있기에 참

if a: # a가 참이라면
    print('참입니다.')
else:
    print('거짓입니다.')
'''