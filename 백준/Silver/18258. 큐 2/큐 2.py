import sys
from collections import deque

# 명령의 수 N을 입력받습니다.
n = int(sys.stdin.readline())

# deque를 생성합니다.
queue = deque()

for _ in range(n):
    # 명령어를 한 줄씩 입력받아 공백을 기준으로 나눕니다.
    command = sys.stdin.readline().split()

    if command[0] == "push":
        queue.append(int(command[1]))

    elif command[0] == "pop":
        if not queue:
            print(-1)
        else:
            # deque의 popleft()는 O(1) 시간 복잡도를 가집니다.
            print(queue.popleft())

    elif command[0] == "size":
        print(len(queue))

    elif command[0] == "empty":
        if not queue:
            print(1)
        else:
            print(0)

    elif command[0] == "front":
        if not queue:
            print(-1)
        else:
            print(queue[0])

    elif command[0] == "back":
        if not queue:
            print(-1)
        else:
            print(queue[-1])