import sys

input = sys.stdin.readline

n = int(input())
f = int(input())

result = 0

result = n//100 * 100

while result % f > 0:
    result += 1
    
result_str = str(result)

#뒤에서부터 문자열 슬라이싱 
print(result_str[-2:])
    
    