import sys
from collections import deque

# 빠른 입력을 위한 설정
input = sys.stdin.readline

# 돌의 개수 n, 점프 조건 제한값 k 입력
n, k = map(int, input().split())

# 각 돌의 높이 정보 입력
stone = list(map(int, input().split()))

# 각 돌에 도달 가능한지를 표시하는 리스트 (0: 도달 불가, 1: 도달 가능)
reached = [0 for _ in range(n)]

# BFS를 위한 큐 생성. 시작점은 첫 번째 돌 (인덱스 0)
q = deque([0])
reached[0] = 1  # 시작점은 도달 가능하므로 표시

# BFS 탐색 시작
while q:
    a = q.popleft()  # 현재 위치한 돌의 인덱스

    # 다음 돌 b는 항상 a보다 오른쪽이어야 하므로 a+1부터 n-1까지 탐색
    for b in range(a + 1, n):
        # 점프 조건 계산
        # (거리) * (1 + 높이 차이) <= k
        if (b - a) * (1 + abs(stone[a] - stone[b])) <= k and not reached[b]:
            # b번 돌에 처음 도달한 경우
            reached[b] = 1  # 도달 가능 표시
            q.append(b)     # 큐에 추가하여 다음 탐색 준비

            # 만약 도착점(N번째 돌)에 도달했다면 바로 YES 출력 후 종료
            if b == n - 1:
                print('YES')
                sys.exit(0)

# 모든 경로 탐색해도 마지막 돌에 도달하지 못했다면 NO 출력
print('NO')
