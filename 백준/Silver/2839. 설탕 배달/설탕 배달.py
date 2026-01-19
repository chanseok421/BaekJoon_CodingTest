import sys

input = sys.stdin.readline


# N kg 배달해야할때 최대한 적은 봉지 가져가기 단위는 5kg, 3kg

n = int(input())

count = 0

while n >= 0:
    if n % 5 == 0:
        count += n // 5
        print(count)
        break
    elif n % 5 != 0:
        n -= 3
        count += 1

else:
    print(-1)
    