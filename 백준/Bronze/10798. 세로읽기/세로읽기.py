# 5줄의 문자열을 입력받아 리스트에 저장
lines = [input() for _ in range(5)]

# 결과를 저장할 빈 문자열 생성
result = ""

# 최대 15칸(열)까지 반복 (문제 조건 최대 길이)
for col in range(15):
    # 각 행에 대해 반복
    for row in range(5): # 5줄을 하나씩 검사
        # 현재 row의 길이가 col 보다 길면 해당 문자를 result에 추가
        if col < len(lines[row]):  # 현재 열 인덱스가 그 줄 길이보다 짧으면 (즉, 글자가 있으면)
            result += lines[row][col] # 그 글자를 결과에 추가

# 결과 출력
print(result)
