# 정수 N을 입력받음
N = int(input())

# N이 0이면 팩토리얼은 1로 정의되어 있음
if N == 0:
    print(1)
else:
    result = 1  # 팩토리얼 결과를 저장할 변수 초기화
    # 2부터 N까지의 숫자를 차례로 곱함
    for i in range(2, N + 1):
        result *= i
    print(result)  # 결과 출력
