#1
'''
print(7 + 3)

result = 7 + 3
print(result)
'''

#2
#주어진 실수 3.1415를 소수점 두 번째 자리에서 반올림하는 파이썬 코드를 작성하세요.
'''
rounded_value = round(3.1415, 2)
#round(a, b) #a를 소수점 b번째 자리에서 반올림
print(rounded_value) #3.14
'''

#3
#주어진 문자열 'Hello, World!'에서 첫 번째 단어 'Hello'만 추출하는 파이썬 코드를 작성하세요.
'''
a = 'Hello, World!'
print(a[:5])

first_word = a.split(',')[0]
#a를 ,기준으로 나눠 0번째를 first_word에 저장
print(first_word)
'''

#자유 1
'''
a = 'Hello, World!'
second_word = a.split(',')[1].lstrip()
#a를 ,기준으로 나눠 leftstrip을 없애 1번째를 second_word에 저장 
print(second_word)
'''

#4
'''
text = 'Python'
changed_text = text.upper()
print(changed_text)
'''

#5
'''
#주어진 리스트 [1, 2, 3, 4, 5]에서 첫 번째 원소와 마지막 원소를 교환하는 파이썬 코드를 작성하세요.
list1 = [1, 2, 3, 4, 5]
list1[0],list1[-1] = list1[-1], list1[0]
print(list1) # [5, 2, 3, 4, 1]
'''

#6
'''
my_list = [5, 2, 7, 1, 9]
my_list.sort()
print(my_list)
'''

#7
'''
t1 = ('apple', 'banana', 'cherry')
element1 = t1[0]
print(element1)
'''

#8
'''
t1 = (1, 2, 3)
t2 = (4, 5, 6)
print(t1 + t2)

merged_tuple = t1 + t2
print(merged_tuple)
'''

#9
'''
dic1 = {'apple' : 3, 'banana' : 5, 'cherry' : 2}
print(dic1['banana'])

bababa_value = dic1['banana']
print(bababa_value)
'''

#10
'''
dic1 = {'apple' : 3, 'banana' : 5, 'cherry' : 2}
dic1['orange'] = 4
print(dic1)
'''

#11
'''
s1 = {1, 2, 3}
s2 = {2, 3, 4}
intersection_of_s1s2 = s1 & s2
print(intersection_of_s1s2)
'''

#12
b1 = True
b2 = False
result = b1 and b2
print(result)