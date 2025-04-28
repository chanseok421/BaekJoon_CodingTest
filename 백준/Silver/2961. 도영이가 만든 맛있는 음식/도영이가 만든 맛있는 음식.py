import sys 
from itertools import combinations

input = sys.stdin.readline

n = int(input())
ing = [tuple(map(int, input().split())) for _ in range(n)] #각 재료의 신맛, 쓴맛 튜플로 저장
differ = 1e9

for i in range(1, n+1):
    cases = combinations(range(n), i)
    
    for case in cases:
        sour = 1 #곱
        bitter = 0 #합
        
        for j in case:
            sour *= ing[j][0]  # 선택한 재료의 신맛 곱
            bitter += ing[j][1]  # 선택한 재료의 쓴맛 합

        differ = min(differ, abs(sour - bitter))  # 최소 차이 갱신

print(int(differ))



