from collections import deque

n, k = map(int, input().split())


circle = deque(range(1, n+1))
result = []

while len(circle) > 0:
    for _ in range(k-1):
        circle.append(circle.popleft()) #k-1번회전
    result.append(circle.popleft()) #k번째 사람 제거
print(f"<{', '.join(map(str, result))}>")
        