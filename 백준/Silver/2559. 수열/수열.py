import sys

input = sys.stdin.readline
n, k = map(int, input().split())

temps = list(map(int, input().split()))

# 첫 번째 윈도우의 합을 계산
current_sum = sum(temps[:k])
max_sum = current_sum

# 윈도우를 슬라이딩하면서 최댓값을 찾음
for i in range(k, n):
    # 윈도우를 한 칸 오른쪽으로 이동
    # 새로 들어온 값(temps[i])을 더하고, 빠져나간 값(temps[i-k])을 뺌
    current_sum = current_sum + temps[i] - temps[i-k]
    
    # 현재 합이 최댓값보다 크면 갱신
    if current_sum > max_sum:
        max_sum = current_sum

print(max_sum)