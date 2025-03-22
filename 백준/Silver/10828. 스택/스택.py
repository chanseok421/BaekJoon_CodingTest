import sys  

n = int(sys.stdin.readline())

stack = []

for _ in range(n):
    cmd = sys.stdin.readline().strip().split()
    
    if cmd[0] == "push":
        stack.append(int(cmd[1]))
    elif cmd[0] == "pop":
        print(stack.pop() if stack else -1)  #stack이 비어있지 않으면 참 > 스택 맨위에서 꺼냄 / stack이 비어져 있으면 것짓 > -1 출력
        
    elif cmd[0] == "size":
        print(len(stack))
        
    elif cmd[0] == "empty":
        print(0 if stack else 1)
        
    elif cmd[0] == "top":
        print(stack[-1] if stack else -1)