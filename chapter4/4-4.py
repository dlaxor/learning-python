# 프로그램의 입출력

import sys

'''
args = sys.argv[0:]
for i in args:
    print(i)
'''

args = sys.argv[1:]
for i in args:
    print(i.upper(), end=' ')