### 파일 읽고 쓰기

# open 함수
# 파일 이름, 파일 열기 모드를 입력값으로 받고, 결괏값 파일 객체를 리턴한다.

# 파일_객체 = open(파일_이름, 파일_열기_모드)
# r (read): 읽기 모드. 파일을 읽기만 할 때 사용한다.
# w (write): 쓰기 모드. 파일에 내용을 쓸 때 사용한다. # 원래 존재하던 파일에 이 함수를 사용하면 있던 내용이 다 사라진다
# a (append): 추가 모드. 파일의 마지막에 새로운 내용을 추가할 때 사용한다.

'''
f = open('새파일.txt', 'w')
f.close()
'''

## 경로지정법
'''
f = open('doit/새파일.txt', 'w')
f.close()
'''
## 쓰는법 - .write(x) # w
'''
f = open('새파일2.txt', 'w', encoding='utf-8')
f.write('안녕하세요')
f.close
'''

'''
f = open('C:/doit/새파일.txt', 'w', encoding='utf-8')
for i in range(1, 11):
    data = f'{i}번째 줄입니다.\n'
    f.write(data)
f.close
'''

#실행하면 한글이 깨져보인다.
'''
f = open('새파일.txt', 'w')
for i in range(1, 11):
    data = f'{i}번째 줄입니다.\n'
    f.write(data)
f.close
'''
#안깨지는 법
'''
f = open('새파일.txt', 'w', encoding='utf-8')
for i in range(1, 11):
    data = f'{i}번째 줄입니다.\n'
    f.write(data)
f.close
'''

## 읽는법 # r

# 첫 한 줄 읽는법 # .readline()
'''
f = open('C:/doit/새파일.txt', 'r', encoding='utf-8')
line = f.readline()
print(line)
f.close()
'''

# 응용
# readline을 반복실행하면 계속 한 줄씩 내려감
'''
f = open('C:/doit/새파일.txt', 'r', encoding='utf-8')
while True:
    line = f.readline()
    if not line:
        break
    print(line) #print에도 줄바꿈, 원래 line에도 \n 포함
f.close()
'''

# readlines()
# 파일의 모든 줄을 읽어서 각각의 줄을 요소로 가지는 리스트를 리턴
'''
f = open('C:/doit/새파일.txt', 'r', encoding='utf-8')
lines = f.readlines()
print(lines)
f.close()
#['1번째 줄입니다.\n', '2번째 줄입니다.\n', '3번째 줄입니다.\n', '4번째 줄입니다
#.\n', '5번째 줄입니다.\n', '6번째 줄입니다.\n', '7번째 줄입니다.\n', '8번째 줄 
#입니다.\n', '9번째 줄입니다.\n', '10번째 줄입니다.\n']
'''
# 응용
'''
f = open('C:/doit/새파일.txt', 'r', encoding='utf-8')
lines = f.readlines()
for i in lines:
    print(i, end='') #i = i.strip(), i = i.replace('\n', '')
f.close()
'''

# read
# 파일 전체를 str으로 리턴한다
'''
f = open('C:/doit/새파일.txt', 'r', encoding='utf-8')
data = f.read()
print(data)
f.close()
'''

# 파일을 리스트처럼 사용할 수도 있다
'''
f = open('C:/doit/새파일.txt', 'r', encoding='utf-8')
for i in f: # f에서 한 줄씩 뽑아온다
    print(i, end='')
f.close()
'''

## 파일에 새로운 내용 추가하기 # a
# w말고 a쓰는 이유 : w는 덮어쓰기, a는 추가하기
'''
f = open('C:/doit/새파일.txt', 'a', encoding='utf-8')
for i in range(11, 21):
    data = f'{i}번째 줄입니다 \n'
    f.write(data)
f.close()
'''

# with문과 함께 사용해 close()를 안써도 되게 할 수도 있다
# f를 지역변수로 만들어버린다
# with문을 벗어나는 순간, 열린 파일 객체 f가 자동으로 닫힌다.
with open('foo.txt', 'w') as f: # f에 open('foo.txt', 'w') 담기
    f.write('life is too short, you need python')