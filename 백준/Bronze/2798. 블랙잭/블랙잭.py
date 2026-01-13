import sys

input = sys.stdin.readline

n, m = map(int, input().split())

cards = list(map(int, input().split()))

current_m = 0
result = 0


    
cards.sort()

for i in range(n):
    for j in range(i+1, n):
        for k in range(j+1, n):
            
            current_m = cards[i] + cards[j] + cards[k]
            
            if current_m <= m and current_m > result:
                result = current_m

print(result)
                
