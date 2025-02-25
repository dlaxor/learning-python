# mod1.py

def add(a, b):
    return a + b

def sub(a, b):
    return a - b

# 다른 파일에서 이 모듈을 import해서 사용할 때,
# 모듈 파일에서만 실행하고 싶은 명령어가 있다면?
if __name__ == '__main__':
    print(add(1,2))