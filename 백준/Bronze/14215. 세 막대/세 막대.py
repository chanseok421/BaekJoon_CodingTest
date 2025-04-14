a, b, c = map(int, input().split())

s = sorted([a,b,c])

if s[2] >= s[0] + s[1]:
    s[2] = s[0] + s[1] - 1
    
print(sum(s))