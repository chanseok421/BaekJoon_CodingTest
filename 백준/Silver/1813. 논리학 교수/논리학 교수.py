import sys
from collections import Counter

input = sys.stdin.readline

N = int(input())

statements = list(map(int, input().split()))

counts= Counter(statements)

answer = []

for i in range(N + 1):
    if counts[i] == i:
        answer.append(i)
        
if answer:
    print(max(answer))
else:
    print(-1)
    