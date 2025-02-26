import os

'''
def search(dirname):
    filenames = os.listdir(dirname) # os.listdir를 사용하면 해당 디렉터리에 있는 파일의 리스트
    for i in filenames:
        full_filename = os.path.join(dirname, i) # dirnamem과 i 사이에 / 추가
        ext = os.path.splitext(full_filename)[-1]
        if ext == '.py':
            print(full_filename)

search('c:/python/')
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