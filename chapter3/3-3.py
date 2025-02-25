# for 문

# for문의 기본 구조
'''
for 변수 in 리스트(또는 튜플, 문자열):
    수행할_문장1
    수행할_문장2
    ...
'''

# 전형적인 for 문
'''
test_list = ['one', 'two', 'three']
for i in test_list:
    print(i)
'''
'''
a = [(1, 2), (3, 4), (5, 6)]
for (first, last) in a:
    print(first + last)
'''

# for문 응용하기
'''
marks = [90, 25, 67, 45, 80]

number = 0
for mark in marks:
    number = number + 1
    if mark >= 60:
        print(f'({number}번 학생은 합격입니다.)')
    else:
        print(f'({number}번 학생은 불합격입니다.)')
'''

# for문과 continue문
'''
marks = [90, 25, 67, 45, 80]

number = 0
for mark in marks:
    number += 1
    if mark < 60:
        continue
    print(f'({number}번 학생, 합격을 축하합니다)')
'''

# for문과 함께 자주 사용되는 range 함수
# c = range(a, b) a이상 b미만의 range객체를 만들어준다.
# 1부터 10까지 더하는 예제
'''
add = 0
for i in range(1, 11):
    add = add + i
print(add)
'''

# for과 range를 사용하여 구구단 만들기
'''
for i in range(2, 10):
    for j in range(1, 10):
        print(i * j, end =' ') # end = 'x'는 print함수가 끝나고 \n하는 대신 x를 출력하는것으로 대체시키는 기능
    print('') #print함수는 \n이 내재되어있다
'''

#
a = [1, 2, 3, 4]
result = []
for num in a:
    result.append(num * 3)
print(result)