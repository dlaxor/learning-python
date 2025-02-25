### 표준 라이브러리

## datetime.date
import datetime
day1 = datetime.date(2021, 12, 14)
day2 = datetime.date(2023, 4, 5)

#print(day1)

diff = day2 - day1
#print(diff.days)

#print(day1.weekday())
#print(day1.isoweekday())


## time
import time
'''
a = time.time()

for i in range(1, 1001):
    print(i)

b = time.time()

print(b-a)

a = time.time()
#print(a)

b = time.localtime(time.time())
#print(b)

c = time.asctime(time.localtime(time.time()))
#print(c)

d = time.ctime()
#print(d)

e = time.strftime('%a', time.localtime(time.time()))
#print(e)

import time
for i in range(1, 11):
    print(i)
    time.sleep(1)
'''


## random
'''
import random

a = random.random() # 0 ~ 1
#print(a)

b = random.randint(1, 10) # 1 ~ 10
#print(b)

import random
def random_pop(data):
    num = random.randint(0, len(data)-1)
    return data.pop(num)

if __name__ == '__main__':
    data = [1, 2, 3, 4, 5]
    while data:
        print(random_pop(data))
        time.sleep(0.25)
'''


## itertools.zip_longest
# zip + 남은거 채우기기능
import itertools

students = ['한민서', '황지민', '이영철', '이광수', '김승민']
snacks = ['사탕', '초컬릿', '젤리']

result = itertools.zip_longest(students, snacks, fillvalue='새우깡')
#print(list(result))


## itertools.permutation # nPr
import itertools

a = list(itertools.permutations(['1', '2', '3'], 2))
#print(a)
'''
for a, b in (itertools.permutations(['1', '2', '3'], 2)):
    print(a + b)
'''


## itertools.combination # nCr
'''
import itertools
it = itertools.combinations(range(1, 46), 6)

for i in it:
    print(i)
'''

## functools.reduce
# 함수(function)를 반복 가능한 객체(iterable)의 요소에 차례대로
# 누적 적용하여 이 객체를 하나의 값으로 줄이는 함수
import functools

data = [1, 2, 3, 4, 5]
result = functools.reduce(lambda x, y: x + y, data)
#print(result)  # ((((1+2)+3)+4)+5)

num_list = [3, 2, 8, 1, 6, 7]
max_num = functools.reduce(lambda x, y: x if x > y else y, num_list)
#print(max_num)  # 8 출력


## operator.itemgetter
from operator import itemgetter

students = [
    ("jane", 22, 'A'),
    ("dave", 32, 'B'),
    ("sally", 17, 'B'),
]

result = sorted(students, key=itemgetter(1))
#print(result)

students = [
    {"name": "jane", "age": 22, "grade": 'A'},
    {"name": "dave", "age": 32, "grade": 'B'},
    {"name": "sally", "age": 17, "grade": 'B'},
]

result = sorted(students, key=itemgetter('age'))
#print(result)


## shutill
import shutil
#shutil.copy("c:/python/free.py", "c:/python/free2.py")


## glob
import glob

#print(glob.glob('c:/python/chapter2/2*'))

import urllib.request


## urllib
def get_wikidocs(page):
    resource = 'https://wikidocs.net/{}'.format(page)
    with urllib.request.urlopen(resource) as s:
        with open('wikidocs_%s.html' % page, 'wb') as f:
            f.write(s.read())

#get_wikidocs(12)


## webbrowser

import webbrowser

webbrowser.open_new('http://python.org')
webbrowser.open('http://python.org')