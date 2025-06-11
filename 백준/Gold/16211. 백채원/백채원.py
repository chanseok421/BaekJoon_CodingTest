import sys
import heapq

# 빠른 입력
input = sys.stdin.readline

# 입력 처리
N, M, K = map(int, input().split())  # N: 지점 수, M: 도로 수, K: 추종자 수

# 그래프 초기화 (인접 리스트)
graph = [[] for _ in range(N + 1)]

# 도로 정보 입력
for _ in range(M):
    a, b, t = map(int, input().split())
    graph[a].append((b, t))
    graph[b].append((a, t))  # 양방향 그래프

# 추종자들이 위치한 지점 리스트
followers = list(map(int, input().split()))

# 다익스트라 함수 (여러 시작점을 한 번에 처리)
def dijkstra(start_nodes):
    INF = int(1e18)
    dist = [INF] * (N + 1)  # 최단거리 배열 초기화
    heap = []

    # 여러 시작점: 각각 거리 0으로 세팅
    for node in start_nodes:
        dist[node] = 0
        heapq.heappush(heap, (0, node))  # (거리, 정점) 형태로 push

    while heap:
        d, u = heapq.heappop(heap)  # 가장 가까운 정점 꺼냄
        if d > dist[u]:  # 이미 더 짧은 경로로 방문했으면 skip
            continue

        for v, w in graph[u]:  # 인접한 정점들 탐색
            if dist[v] > d + w:  # 더 짧은 경로 발견 시 갱신
                dist[v] = d + w
                heapq.heappush(heap, (dist[v], v))
    return dist

# 1번 지점(대구과학고)에서 출발하는 최단 거리 배열
dist_from_1 = dijkstra([1])

# 추종자들이 각자 출발하는 최단 거리 배열
# 다중소스 다익스트라로, 모든 추종자들이 출발하는 것을 한 번에 계산
dist_from_followers = dijkstra(followers)

# 조건을 만족하는 집 후보 지점 찾기
result = []
for i in range(2, N + 1):  # 집 후보는 2번 ~ N번
    if dist_from_1[i] < dist_from_followers[i]:
        result.append(i)

# 출력: 조건을 만족하는 집 후보를 오름차순 출력 (없으면 0 출력)
if result:
    print(' '.join(map(str, sorted(result))))
else:
    print(0)
