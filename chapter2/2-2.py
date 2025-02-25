'''
print("=" * 50)
print("My program")
print("=" * 50)
'''

#b = 'what have we done'

#a = b[0] + b[1] + b[2] + b[3]

#print(len(b))
# = 17
#len은 인덱싱, 슬라이싱할때의 숫자가 아니라 실제 길이를 나타냄

#print(b[::]) a:b:c (a이상 b미만 c만큼의 간격)
'''
a = '20230331Rainy'
date = a[:8]
weather = a[8:]
year = a[:4]
month = a[4:6]
day = a[6:8]
print(date)
print(weather)
print(year, month, day)
'''

#문자열 포맷팅
'''
#a = "I eat %d apples." %10
number = 10
day = "three"
#a = "I eat %s apples" %day
#a = "I eat %d apples" %number
a = "I ate %d apples. So i was sick for %s days." %(number, day)

print(a)

a = "%0.5f" %3.141592
print(a)


a = "I eat {0} {1}.".format(5, "apples")
a = "I eat {number} {fruit}".format(number = 5, fruit = "apples")
print(a)


#정렬
a = "{0:>10}".format("Hi")
#a = "{0:^10}".format("Hi")
#a = "{0:<10}".format("Hi")
print(a)


#중요한 문자열 포맷팅 (f) importance : OOOOO
name = '임택'
age = 20.3206892345
#a = f'나의 이름은 {name}입니다. 내 만 나이는 {age-2}입니다.'
#a = f'{"hi":>10}'
#a = f'{age:0.4f}'
a = 10000000000000
print(f"{a:,}")
'''

#문자열 관련 함수들
'''
#a = "hobby"
#print(a.count('b'))
#print(a.find('b')) # = 2 (0 1 2)
#print(a.index('b'))
#find index 차이 : find는 없는거검색하면 -1, index는 오류

a = ", ".join('abcd')
print(a) #a, b, c, d

a = "HI"
print(a.lower()) # = hi #lower upper

a = " hi "
print(a.rstrip()) #공백없애기 lstrip strip rstrip

a = "what have we done" #replace (ctrl f)
print(a.replace("we", "you"))

#a = "what have we done"
#print(a.split())
a = "what:have:we:done"
print(a.split(":")) #split하는 기준을 :로 세움
'''