import sys

input= sys.stdin.readline

n = int(input())

arr_a =[]
arr_b =[]

result1 = 0
result2 = 0
result = 0

for _ in range(n):
    a, b = map(int, input().split())
    arr_a.append(a)
    arr_b.append(b)

result1 = max(arr_a) - min(arr_a)
result2 = max(arr_b) - min(arr_b)

result = result1 * result2
print(result)



    