import sys
from itertools import combinations

input = sys.stdin.readline

n = int(input())
min_p, min_f, min_s, min_v = map(int, input().split())

ingredients = []
for _ in range(n):
    p, f, s, v, c = map(int, input().split())
    ingredients.append((p, f, s, v, c))

min_cost = float('inf')
result = []

for i in range(1, n+1):
    for comb in combinations(range(n), i):
        p_sum = f_sum = s_sum = v_sum = c_sum = 0
        for idx in comb:
            p, f, s, v, c = ingredients[idx]
            p_sum += p
            f_sum += f
            s_sum += s
            v_sum += v
            c_sum += c
        if p_sum >= min_p and f_sum >= min_f and s_sum >= min_s and v_sum >= min_v:
            if c_sum < min_cost:
                min_cost = c_sum
                result = [comb]
            elif c_sum == min_cost:
                result.append(comb)

if not result:
    print(-1)
else:
    result.sort()
    print(min_cost)
    print(' '.join(str(i+1) for i in result[0]))
