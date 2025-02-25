#딕셔너리 #대응 관계를 나타낼 수 있는 자료형
'''
dic1 = {'name' : 'Taek', 'phone number' : '010-8655-2378', 'birth' : '1215'}
print(dic1) #{'name': 'Taek', 'phone number': '010-8655-2378', 'birth': '1215'}

#딕셔너리 안에 list도 넣을 수 있습니더
dic2 = {'a' : [1, 2, 3], 'b' : 2, 5 : 6}
print(dic2)
'''

#딕셔너리에 값 추가하는 방법
'''
dic3 = {'a' : 3}
dic3['b'] = 2 #dic[KEY] = VALUE #숫자는 따옴표가 필요없음
print(dic3) #하지만 문자열로 사용하고싶다면 해야겠지

#딕셔너리 값 삭제하는법
dic1 = {'name' : 'Taek', 'phone number' : '010-8655-2378', 'birth' : '1215'}
del dic1['name'], dic1['phone number'] #del은 쉼표기용 가능
print(dic1) #{'birth': '1215'}
'''

#딕셔너리 활용법
'''
TaekInfo = {'name' : 'Taek', 'phone number' : '010-8655-2378', 'birth' : '1215'}
print(TaekInfo['name']) #key를 통해서 value를 가져온다
#주의사항 : key는 중복, 변형, mutable 자료형 불가
'''

#keys, values 찾는법
'''
#keys
dic5 = {'a' : 1, 'b' : 2, 'c' : 3}
print(dic5.keys()) # dict_keys(['a', 'b', 'c'])
#파이썬 2.7 버전까지는 a.keys() 함수를 호출하면 dict_keys가
#아닌 리스트를 리턴한다. 리스트를 리턴하기 위해서는
#메모리 낭비가 발생하는데, 파이썬 3.0 이후 버전에서는
#이러한 메모리 낭비를 줄이기 위해 dict_keys 객체를 리턴하도록 변경되었다.

#리스트가 필요한 경우에는 list(a.keys())를 사용하면 된다.
print(list(dic5.keys())) # ['a', 'b', 'c']

#values
print(dic5.values()) # dict_values([1, 2, 3])
print(list(dic5.values())) # [1, 2, 3]

#keys, values
print(dic5.items()) # dict_items([('a', 1), ('b', 2), ('c', 3)])
# items 함수는 Key와 Value의 쌍을 튜플로 묶은 값을 dict_items 객체로 리턴
'''

#key : value 쌍 값 모두 지우기
'''
dic5 = {'a' : 1, 'b' : 2, 'c' : 3}
dic5.clear()
print(dic5) # {}
#clear함수는 딕셔너리 뿐만 아니라 리스트, 집합 등의 mutable 자료형에서 사용가능
#하지만 clear함수는 만두소를 없애는것. 만두피까지 없애려면 del dic5
'''

#key로 value얻는법 두번째 - get
'''
dic5 = {'a' : 1, 'b' : 2, 'c' : 3}
print(dic5['a']) #원래는 이렇게
print(dic5.get('a')) #get
#원래 없는 키 쓰면 에러가 남. 근데 get은 none이라고 뜸

#get 활용
print(dic5.get('d', 'there is no d'))
#dic5에 d라는 key가 있는지 보고, 없으면 there is no d라고 출력하거라
'''

# 해당 Key가 딕셔너리에 있는지 보기 - in

dic5 = {'a' : 1, 'b' : 2, 'c' : 3}
print('a' in dic5) #key a가 dic5에 있니? #True
print('d' in dic5) #key d가 dic5에 있니? #false