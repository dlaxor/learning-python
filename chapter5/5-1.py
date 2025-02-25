### 클래스
### 반복되는 변수와 메서드*를 미리 정해놓은 틀(설계도) *클래스 안에 존재하는 함수

# 클래스를 사용하지 않았을 때
# 같은 함수를 여러 줄 써야 함
'''
result = 0
result2 = 0

def add(num):
    global result
    result += num
    return result

def add2(num):
    global result2
    result2 += num
    return result2

print(add(3))
print(add(4))
print(add2(5))
print(add2(7))
'''

## 클래스 만드는법
'''
class Cookie: # 클래스 전통 대문자로 시작
    pass

chokolate_cookie = Cookie()
amond_cookie = Cookie()
'''

## 계산기를 만들어보자
'''
class FourCal:
    def setdata(self, first, second): # 내부함수 = 메서드
        self.first = first # a와 같은 객체들은 self이다. 그 self들의 first와 second에 값을 지정해준다 
        self.second = second
    def add(self):
        result = self.first + self.second
        return result
    def sub(self):
        result = self.first - self.second
        return result
    def mul(self):
        result = self.first * self.second
        return result
    def div(self):
        result = self.first / self.second
        return result

a = FourCal()
b = FourCal()

a.setdata(4, 2) # a = self, 4 = first, 2 = second
print(a.add())
print(a.sub())
print(a.mul())
print(a.div())

b.setdata(7, 4)
print(b.add())
print(b.sub())
print(b.mul())
print(b.div())
'''
## 생성자
# 객체가 생성될 때 자동으로 호출되는 메서드
# 위 계산기에서, setdata를 입력하지 않고 실행하면 오류가 뜬다.
# 만약 setdata 입력을 강제했다면, 이런 오류를 방지할 수 있었을 것이다.
# 그래서 생성자를 응용할 수 있다

class FourCal:
    def __init__(self, first, second): # __init__ = 생성자
        self.first = first
        self.second = second
    def setdata(self, first, second):
        self.first = first
        self.second = second
    def add(self):
        result = self.first + self.second
        return result
    def sub(self):
        result = self.first - self.second
        return result
    def mul(self):
        result = self.first * self.second
        return result
    def div(self):
        result = self.first / self.second
        return result

'''
a = FourCal() # 그냥 실행하면 오류가 뜸.
a = FourCal(4, 2)
# 오류를 해결하려면 다음처럼 first와 second에 해당하는 값을 전달하여 객체를 생성해야 한다.
'''

## 클래스의 상속
# 상속 개념을 사용하여 우리가 만든 FourCal 클래스에 a^b값을 구할 수 있는 기능을 추가해 보자.

class MoreFourCal(FourCal): # class 클래스_이름(상속할_클래스_이름)
    def power(self):
        result = self.first ** self.second
        return result

# MoreFourCal 클래스는 FourCal 클래스를 상속했으므로 FourCal 클래스의 모든 기능을 사용할 수 있다.
'''
a = MoreFourCal(4, 2)
print(a.add()) # 6

b = MoreFourCal(6, 2)
print(b.power()) # 36
'''

## 메서드 오버라이딩
# FourCal 클래스의 객체 a에 값 4와 0을 지정하고 div 메서드를 호출하면
# 4를 0으로 나누려고 하므로 ZeroDivisionError 오류가 발생한다.
# 0으로 나눌 때 오류가 아닌 값 0을 리턴받고 싶다면 어떻게 해야 할까?

class SafeFourCal(FourCal):
    def div(self):
        if self.second == 0:
            return 0
        else:
            return self.first / self.second
'''
a = SafeFourCal(4, 0)
print(a.div()) # 0
'''

## 클래스변수
# 객체변수는 다른 객체들의 영향을 받지 않고 # * first, second
# 독립적으로 그 값을 유지한다는 점을 이미 알아보았다.
# 객체변수와는 성격이 다른 클래스변수에 대해 알아보자.

class Family:
    lastname = '김' # lastname == 클래스변수

a = Family()
b = Family()

a.lastname = '박'

print(a.lastname) # 박
print(b.lastname) # 김
# 다른 인스턴스(객체)이더라도 동일한 클래스에서 동일한 값을 얻고싶다면
# 클래스변수를 사용한다 (각각은 self, ~, ~~)