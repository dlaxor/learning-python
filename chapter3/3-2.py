# 반복문

# 1. while문
# 문장을 반복해서 수행해야 할 경우 사용함

# 다음은 while 문의 기본 구조이다.
'''
while 조건문:
    수행할_문장1
    수행할_문장2
    수행할_문장3
    ...
'''

# ‘열 번 찍어 안 넘어가는 나무 없다’라는 속담 표현하기
'''
treeHit = 0 # treeHit는 while문의 조건 부분에서 쓰이는 변수이기에 초기값 필수

while treeHit < 10:
    treeHit = treeHit + 1 # 줄여서 treeHit += 1
    print("나무를 %d번 찍었습니다" %treeHit)
    if treeHit == 10:
        print("나무가 넘어갔습니다.")
'''

# 4를 입력하지 않으면 계속 print하고 4를 입력했을때만 종료되는 예제
"""
prompt = '''
1. Add
2. Del
3. List
4. Quit

Enter number : '''

number = 0

while number != 4:
    print(prompt)
    number = int(input())
    if number == 4:
        print('종료')
"""

# break (while문 강제로 빠져나가기)
'''
coffee = 10
price_coffee = 300
money = 3000

while money >= price_coffee:
    print('커피를 받았습니다.')
    coffee = coffee - 1
    money = money - price_coffee
    print('남은 커피의 양은 %d개 입니다.' %coffee)
    if coffee == 0:
        print('커피가 소진되었습니다. 판매를 중지합니다.')
        break
    if money < price_coffee:
        print('돈이 부족합니다.')
        break
'''
'''
coffee = 10

while coffee >= 0:
    if coffee == 0:
        print('커피가 부족합니다. 판매를 중지합니다.')
        break

    print('돈을 내십시오.')

    money = int(input())
    if money < 0:
        print('잘못된 값을 입력하였습니다.')
        break

    if money == 300:
        print('커피 나왔습니다.')
        coffee = coffee - 1
    elif money > 300:
        print('커피 나왔습니다.')
        coffee = coffee - 1
        change = money - 300
        print('거스름돈 : %d' %change)
    else:
        print('돈이 부족합니다.')
        change = money
    print(f'잔여 커피 수 : {coffee}')
'''

# while문의 맨 처음으로 돌아가기 (continue)
# 홀수만 출력되게 하는 예제
'''
a = 0
while a < 10:
    a = a + 1
    if a % 2 == 0:
        continue
    print(a)
'''

# 무한 루프
'''
while True:
    print("무한루프를 강제로 빠져나가는 방법 : Ctrl + C")
'''