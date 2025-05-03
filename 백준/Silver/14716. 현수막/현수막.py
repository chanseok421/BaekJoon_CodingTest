from collections import deque

# 입력
M, N = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(M)]
visited = [[False]*N for _ in range(M)]

# 8방향
dx = [-1, -1, -1, 0, 1, 1, 1, 0]
dy = [-1, 0, 1, 1, 1, 0, -1, -1]

def bfs(x, y):
    queue = deque()
    queue.append((x, y))
    visited[x][y] = True

    while queue:
        cx, cy = queue.popleft()
        for dir in range(8):
            nx = cx + dx[dir]
            ny = cy + dy[dir]
            if 0 <= nx < M and 0 <= ny < N:
                if board[nx][ny] == 1 and not visited[nx][ny]:
                    visited[nx][ny] = True
                    queue.append((nx, ny))

# 전체 순회
count = 0
for i in range(M):
    for j in range(N):
        if board[i][j] == 1 and not visited[i][j]:
            bfs(i, j)
            count += 1

print(count)
