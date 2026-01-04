import sys

# 빠른 입력을 위해 sys.stdin.readline 사용
input = sys.stdin.readline

T = int(input())

for _ in range(T):
    a, b = map(int, input().split())
    
    # a^b를 10으로 나눈 나머지를 구함 (1의 자릿수)
    # pow(a, b, 10)은 내부적으로 효율적인 알고리즘을 사용하여 매우 빠름
    ans = pow(a, b, 10)
    
    # 나머지가 0이라면 10번 컴퓨터가 처리함
    if ans == 0:
        print(10)
    else:
        print(ans)