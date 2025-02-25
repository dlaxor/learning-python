# 구구단

def gugudan(num):
    for i in range(1, 10):
        print(num * i, end = ' ')
    print()

num = int(input('숫자를 입력하세요 : '))
gugudan(num)
