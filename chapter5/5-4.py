### 예외처리

# 구조
'''
try:
     # 오류가 발생할 수 있는 구문
except 발생오류 as 오류변수:
     # 오류가 발생한다면 동작하는 구문
else:
     # 오류가 발생하지 않는다면 동작하는 구문
finally:
     # 무조건 마지막에 실행
'''

## try-except 문
# try블록 에러 -> except블록 수행
try:
    4 / 0
except ZeroDivisionError as e:
    print(e)

## try-finally 문
# try 문 수행 도중 예외 발생 여부에 상관없이 항상 finally 절 수행
try:
    f = open('foo.txt', 'w')
finally:
    f.close()

## 여러가지 에러 처리
try:
    #a = [1, 2]
    #print(a[3])
    4 / 0
except ZeroDivisionError:
    print('0으로 나눌 수 없습니다.')
except IndexError:
    print('인덱싱 할 수 없습니다.')

## try-else 문
# try 문 수행 중 오류가 발생하면 except 절, 오류가 발생하지 않으면 else 절
try:
    age = int(input('나이를 입력하세요 : '))
except:
    print('입력이 정확하지 않습니다.')
else:
    if age <= 18:
        print('미성년자는 출입금지입니다.')
    else:
        print('환영합니다.')

## 오류 회피하기
try:
    f = open('나없는파일', 'r')
except FileNotFoundError:
    pass
print('꼭 작동되어야하는 중요한 코드')

## 오류 일부러 발생시키기
class Bird:
    def fly(self):
        raise NotImplementedError
    
class Eagle(Bird):
    def fly(self):
        print('펄럭펄럭') # 강제로 오버라이딩을 하게 만드는 역할

a = Eagle()
a.fly()

## 예외 만들기
# 프로그램을 수행하다가 특수한 경우에만 예외 처리를 하려고 종종 예외를 만들어서 사용한다.
class MyError(Exception):
    pass

def say_nick(nick):
    if nick == '바보':
        raise MyError()
    print(nick)

## say_nick('바보')

try:
    say_nick('천사')
    say_nick('바보')
except MyError as e:
    print(e)