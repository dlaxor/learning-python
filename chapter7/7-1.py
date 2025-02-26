# 유니코드로 문자열 다루기
'''
a = "Life is too short"
b = a.encode('utf-8')

print(b) # b'Life is too short'
print(type(b)) # <class 'bytes'>
'''

# 아스키로 한글을 다루면?
'''
a = "한글"
a.encode("ascii") # UnicodeEncodeError
'''

# 한글 인코딩
'''
a = '임택'
b = a.encode('utf-8') # b'\xec\x9e\x84\xed\x83\x9d'
print(b)
b = a.encode('euc-kr') # b'\xc0\xd3\xc5\xc3'
print(b)
'''

# 디코딩하기
# x로 인코딩하면 x로 디코딩해야 한다

a = '임택'
b = a.encode('utf-8')
c = b.decode('utf-8')
print(c)