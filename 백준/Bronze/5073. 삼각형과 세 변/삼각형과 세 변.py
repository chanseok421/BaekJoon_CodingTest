while True:
    a, b, c = map(int, input().split())

    if a == 0 and b == 0 and c == 0:
        break

    # 삼각형 성립 조건 먼저 체크
    if a + b <= c or a + c <= b or b + c <= a:
        print("Invalid")
    elif a == b == c:
        print("Equilateral")
    elif a == b or a == c or b == c:
        print("Isosceles")
    else:
        print("Scalene")