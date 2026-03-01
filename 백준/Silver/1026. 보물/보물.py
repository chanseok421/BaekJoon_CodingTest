import sys

N = int(input())

A = sys.stdin.readline().strip().split()
B = sys.stdin.readline().strip().split()

A = [int(x) for x in A]
B = [int(x) for x in B]

ans = 0

for i in range(N):
    ans += min(A) * max(B)
    A.pop(A.index(min(A)))
    B.pop(B.index(max(B)))

print(ans)