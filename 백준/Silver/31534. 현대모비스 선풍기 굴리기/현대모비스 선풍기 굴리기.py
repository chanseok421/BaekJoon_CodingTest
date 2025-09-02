import sys, math

a, b, h = map(int, sys.stdin.readline().split())

# 무한히 이어짐 (원주가 같아 굴려도 주기가 없음)
if a == b:
    print(-1)
    sys.exit(0)

# 원뿔(안쪽 구멍이 없음) : 넓이 = π * (빗변^2) = π * (b^2 + h^2)
if a == 0:
    print((b*b + h*h) * math.pi)
    sys.exit(0)

m = max(a, b)
n = min(a, b)

# 유사삼각형으로 축에서 큰 밑변까지의 거리 x
x = (m * h) / (m - n)

# 큰/작은 원의 반지름 제곱 (빗변^2)
R2 = x*x + m*m
r2 = (x - h)*(x - h) + n*n

area = (R2 - r2) * math.pi
print(area)
