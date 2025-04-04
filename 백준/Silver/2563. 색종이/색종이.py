paper = int(input())
coords = []#좌표

for _ in range(paper):
    a, b = map(int, input().split())
    coords.append((a, b))  
    
# 도화지 100x100 배열 만들기
paper_big = [[0] * 100 for _ in range(100)]

# 색종이 영역 표시
for x, y in coords:
    for i in range(x, x + 10):
        for j in range(y, y + 10):
            paper_big[j][i] = 1  # y가 행(세로), x가 열(가로)

# 덮인 칸 수 계산
result = sum(row.count(1) for row in paper_big)

# 출력
print(result)
