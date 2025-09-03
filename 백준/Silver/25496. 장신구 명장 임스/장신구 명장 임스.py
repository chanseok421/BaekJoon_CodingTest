import sys
input = sys.stdin.readline

P, N = map(int, input().split())
jewels = list(map(int, input().split()))

# 작은 값부터 착용
jewels.sort()

count = 0
for val in jewels:
    if P >= 200:
        break
    P += val
    count += 1

print(count)
