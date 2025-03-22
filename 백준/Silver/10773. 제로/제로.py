import sys

k = int(sys.stdin.readline())

money = []

for _ in range(k):
    
    num = int(sys.stdin.readline())
    
    if num > 0:
        money.append(num)
    elif num == 0:
       if money:
           money.pop()
        
print(sum(money))