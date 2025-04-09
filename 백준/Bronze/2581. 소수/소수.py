m = int(input())
n = int(input())

data = []

    
for x in range(m, n+1):
    if x < 2:
        continue
    for i in range(2, x+1):
        if x % i == 0:
            if x == i:
                data.append(x)
                
            break #약수가 하나라도 나오면 → 소수 아님 → 더 검사할 필요 없음 → 루프 탈출
                
if data:
    print(sum(data))
    print(min(data))
else:
    print(-1)
                
                
        