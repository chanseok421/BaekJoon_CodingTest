t = int(input())  # 테스트 케이스 수 입력

for _ in range(t):  # 테스트 케이스 수 만큼 반복
    a, b = map(int, input().split())  # 두 정수 a, b 입력받기
    
    result = a * b  # a와 b를 곱한 값 저장 (나중에 최소공배수 구할 때 사용)

    # 최대공약수(GCD) 구하기 (유클리드 호제법)
    while b > 0:
        a, b = b, a % b
        
        # tmp = b
        # b = a % b
        # a = tmp
        
    print(result // a)  # 최소공배수(LCM) 출력


# 2
# 6 8
# 10 15

# 실행 과정:

# (6,8) → GCD 2 → LCM = (6×8)//2 = 24

# (10,15) → GCD 5 → LCM = (10×15)//5 = 30

# a | b | 설명
# 48 | 18 | 시작
# 18 | 12 | 48%18=12
# 12 | 6 | 18%12=6
# 6 | 0 | 12%6=0 (끝)