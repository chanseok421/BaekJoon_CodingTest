import sys

input = sys.stdin.readline

a, b, c, d, e = map(int, input().split())

num = (a*a) + (b*b) + (c*c) + (d*d) + (e*e)

psw = num % 10

print(psw)