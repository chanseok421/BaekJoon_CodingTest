# 1. 입력 받기
N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

# 2. 정렬 수행
# A는 오름차순 (작은 수 -> 큰 수)
A.sort()

# B는 내림차순 (큰 수 -> 작은 수)
B.sort(reverse=True)

# 3. S 계산
S = 0
for i in range(N):
    S += A[i] * B[i]

# 4. 출력
print(S)