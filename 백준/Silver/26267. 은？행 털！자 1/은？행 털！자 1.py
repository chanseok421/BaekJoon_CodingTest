import sys
input = sys.stdin.readline

N = int(input().strip())
group = {}
for _ in range(N):
    x, t, c = map(int, input().split())
    key = x - t
    group[key] = group.get(key, 0) + c
    
print(max(group.values()) if group else 0)