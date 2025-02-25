# 특정 디렉터리부터 시작해서 그 하위(디렉터리 포함)의 모든 파일 중 파이썬 파일(*.py)만 출력

import os

'''
def search(dirname):
    filenames = os.listdir(dirname) # os.listdir를 사용하면 해당 디렉터리에 있는 파일의 리스트
    for i in filenames:
        full_filename = os.path.join(dirname, i)
        print(full_filename)

search('c:/')
'''

def search(dirname):
    try:
        filenames = os.listdir(dirname)
        for i in filenames:
            full_filename = os.path.join(dirname, i)
            if os.path.isdir(full_filename):
                search(full_filename)
            else:
                ext = os.path.splitext(full_filename)[-1]
                if ext == '.py':
                    print(full_filename)
    except PermissionError:
        print('접근 권한이 없거나 경로가 잘못되었습니다.')
        
search('c:/python/')