import sys
from collections import deque #파이썬의 deque는 양쪽에서 빠르게 삽이/삭제가 가능한 큐 자료구조 pop(0)쓰는것보다 빠르다

n = int(sys.stdin.readline())        

q = deque()

for _ in range(n):
    
    cmd = sys.stdin.readline().strip().split()
    
    if cmd[0] == 'push':
        q.append(int(cmd[1]))
    elif cmd[0] == 'pop':
        print(q.popleft() if q else -1)
    elif cmd[0] == 'size':
        print(len(q))
    elif cmd[0] == 'empty':
        print(0 if q else 1)
    elif cmd[0] == 'front':
        print(q[0] if q else -1)
    elif cmd[0] == 'back':
        print(q[-1] if q else -1)
         