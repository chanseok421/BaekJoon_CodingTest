import sys

N, S = map(int, sys.stdin.readline().split())
arr = list(map(int, sys.stdin.readline().split()))
ans = 0

def solve(index, current_sum):
    global ans

    if index >= N:
        return

    current_sum += arr[index]

    if current_sum == S:
        ans += 1

    # 현재 원소를 포함하는 경우
    solve(index + 1, current_sum)

    # 현재 원소를 포함하지 않는 경우 (포함했던 원소를 다시 빼줌)
    solve(index + 1, current_sum - arr[index])


solve(0, 0)
print(ans)