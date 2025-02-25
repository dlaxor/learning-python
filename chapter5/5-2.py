### 모듈
## 함수나 변수 또는 클래스를 모아 놓은 파이썬 파일

## 불러오는 법
import mod1
# print(mod1.add(3, 4))

## 필요한 대상만 불러오는 법
from mod1 import add, sub

## 클래스나 변수 등을 포함
import mod2

a = mod2.Math()
# print(a.solv(2))

## 모듈 경로 찾아주기
import sys
sys.path.append('C:/python')
import mod3
# print(a.solv(2))