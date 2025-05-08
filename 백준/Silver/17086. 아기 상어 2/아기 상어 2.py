import sys
from collections import deque

input = sys.stdin.readline

dx = [-1, 1, 0, 0, -1, -1, 1, 1]
dy = [0, 0, -1, 1, -1, 1, -1, 1]


n, m = map(int, input().split())

arr = [list(map(int, input().split())) for _ in range(n)]
q = deque()

result = 0

def bfs():
    while q:
        x, y = q.popleft()
        for d in range(8):
            nx = x + dx[d]
            ny = y + dy[d]
            
            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue
            
            if not arr[nx][ny]:
                arr[nx][ny] = arr[x][y] + 1
                q.append((nx, ny))
                
for x in range(n):
    for y in range(m):
        if arr[x][y]:
            q.append((x,y))

bfs()
for a in arr:
    result = max(max(a), result)
print(result -1)
