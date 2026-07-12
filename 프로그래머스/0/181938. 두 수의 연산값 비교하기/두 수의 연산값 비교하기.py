def solution(a, b):
    answer = int(str(a) + str(b))
    return max(answer, 2*a*b)