#LIST
'''
odd = [1, 3, 5, 7, 9]
#print(type(odd))

e = [1, 'done', ['what', 'have']]
print(e[-1][0]) #list속 list에서 값을 indexing하는 법 (inportant)
print(e[0])
print(e[1][0]) #d

a = [1, 2, 3, 4, 5]
print(a[::2])
# a = '12345' print(a[0:2]) 문자열s 인덱싱이랑 ㅈㄴ똑같음

a = [1, 2, 3]
b = [4, 5, 6]
print(a + b)
print(a*3)
print(len(a)) #list 길이 구하기

#python에서는 서로다른 자료형이 더해지지 않음
print("hi" + str(3))

#list 값 바꾸기
a[1] = 7 #수정
del a[0] #삭제 #슬라이싱으로도 가능 del a[0:2]
print(a)

a = [1, 2, 3]
a.append(4) #list에 값 추가
print(a)

a = [3, 2, 45, 1, 2]
a.sort() #정렬
print(a)

b = ['c', 'a', 'b']
b.sort() #정렬 #문자도 됨
print(b)

c = ['c', 'a', 'b', 'd']
c.reverse() #거꾸로 뒤집기
print(c)

c = ['c', 'a', 'b', 'd']
c.sort()
c.reverse() #정렬하고 뒤집기
print(c)

a = [1, 2, 3]
#print(a.index(3)) #3은 몇번째 인덱스니? = 2
a.insert(0, 4) #append와는 좀 다름 #0번째 인덱스를 4로 만들겠다
print(a) # = [4, 1, 2, 3]

a = [1, 2, 3, 4, 5, 3]
a.remove(3) #remove(x) #첫번째로 나오는 x 삭제
a.remove(3) #두번쓰면 3 다사라짐
print(a)

a = [1, 2, 3]
print(a.pop()) #pop()은 리스트의 맨 마지막 요소를 리턴 후 그 요소 삭제
#리턴하므로 팝한 요소를 프린트해서 볼수있음
print(a)

print(a.pop(0)) #pop(x) 리스트의 x번째 요소를 리턴 후 그 요소 삭제
print(a)

print(a.count(1)) #count(x) 리스트안에 있는 x개수 리턴

a = [1, 2, 3] #extend(x) x에는 리스트만 올수있음
a.extend([4, 5]) # [1, 2, 3, 4, 5]
a.append([4, 5]) # [1, 2, 3, [4, 5]]
print(a)
'''