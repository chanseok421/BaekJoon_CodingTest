import sys

t = int(sys.stdin.readline())



for _ in range(t):
    stack = []
    cmd = sys.stdin.readline().strip()
    
    for ch in cmd:
     if ch == '(':
         stack.append(ch)
     elif ch == ')':
        if stack:
            stack.pop()
        else:
            stack.append('x')
            break
         
    if len(stack) == 0:
        print('YES')
    else:
        print('NO')
         
    

         