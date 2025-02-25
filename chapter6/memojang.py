import sys

print(sys.argv)

option = sys.argv[1]

if option == '-a':
    memo = sys.argv[2]
    f = open('memojang.txt', 'a')
    f.write(memo)
    f.write('\n')
    f.close()
elif option == '-v':
    f = open('memojang.txt', 'r')
    memo = f.read()
    f.close()
    print(memo)