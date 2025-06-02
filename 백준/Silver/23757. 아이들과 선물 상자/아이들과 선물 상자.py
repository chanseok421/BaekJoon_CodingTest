import heapq
import sys

input = sys.stdin.readline

n, m = map(int, input().split())
boxes = list(map(int, input().split()))
wants = list(map(int, input().split()))

# 최대 힙으로 변환
boxes = [-b for b in boxes]  # 음수로 만들어서 최대 힙처럼 동작하게 함
heapq.heapify(boxes)

for want in wants:
    if not boxes:
        print(0)
        exit(0)
    
    largest = -heapq.heappop(boxes)
    
    if largest < want:
        print(0)
        exit(0)
    
    remaining = largest - want
    if remaining > 0:
        heapq.heappush(boxes, -remaining)

print(1)
