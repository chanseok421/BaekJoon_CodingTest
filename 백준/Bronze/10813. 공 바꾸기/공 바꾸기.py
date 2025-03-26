n, m = map(int, input().split())

basketS = list(range(1, n+1))

for _ in range(m):
    i, j  = map(int, input().split())
    basketS[i-1], basketS[j-1] = basketS[j-1], basketS[i-1]


for basket in basketS:
    print(basket, end=' ')


    
