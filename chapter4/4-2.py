# 사용자의 입출력

# input
'''
a = input() #기본은 str으로 받아들인다
print(a)
'''

'''
num = int(input('숫자를 입력하세요 : ')) #숫자로 받아들이고싶으면 int로 감싸줘라
print(num)
'''

# print에 대해 깊이 알아보자
'''
print('life' 'is' 'too' 'short') #lifeistooshort
print('life''is''too''short') #lifeistooshort
print('life'+'is'+'too'+'short') #lifeistooshort
'''
# 문자열 띄어쓰기는 쉼표로 할 수 있다
'''
print('life', 'is', 'too', 'short') #life is too short
'''
# 원래 print는 끝의 기본값이 줄바꿈(\n)이다. 하지만 그걸 end문으로 바꿀 수 있다.
'''
for i in range(1, 11):
    print(i, end = ' ')
# end = 'x' # x = 설정하고픈 끝 값
'''