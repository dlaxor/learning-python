s1 = set([1, 2, 3]) # list를 set함수로 감싼 형태
print(s1) # {1, 2, 3} 

s1 = {1, 3, 3}
print(s1) # {1, 3} # 집합에서 같은원소 두개 허용 안되니께

#그리고 이렇게 s1을 두번 썼다고 s1이 두개인게 아니라 s1을 아랫줄에서 재정의한거임

# =는 같은 값을 가리키게 하는 것 # ==는 같다

#자료형의 참과 거짓
#"python" 참, "" 거짓
#[1, 2, 3] 참, [] 거짓
#(1, 2, 3) 참, () 거짓
#{'a' = 1} 참, {} 거짓
# 1 참, 0 거짓
# None 거짓

a = 'Hello, World!'
second_word = a.split(',')[1].lstrip()
#a를 ,기준으로 나눠 leftstrip을 없애 1번째를 second_word에 저장 
print(second_word)