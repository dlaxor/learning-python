# 게시판 페이징하기
'''
def get_total_page():
    m = int(input('게시물의 총 개수를 입력하세요 : '))
    n = int(input('한 페이지에 보여줄 게시물의 개수를 입력하세요 : '))

    if m % n == 0:
        print(m//n)
    if m % n > 0:
        print(m//n + 1)

    
get_total_page()
'''

# m == 게시물의 총 개수
# n == 한 페이지에 보여줄 게시물의 개수

def get_total_page(m, n):
    if m % n == 0:
        return m//n
    if m % n > 0:
        return m//n + 1

print(get_total_page(45, 2))