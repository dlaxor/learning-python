# 문서 파일을 읽어서 그 문서 파일 안에 있는 탭 문자(Tab)를 공백 문자(Space) 4개로 바꾸어 주는 스크립트

import sys

src = sys.argv[1]
dst = sys.argv[2]

#print(src)
#print(dst)

f = open(src, 'r')
tab_content = f.read()
f.close

space_content = tab_content.replace('/t', ' '*4)
#print(space_content)

f = open(dst, 'w')
f.write(space_content)
f.close()