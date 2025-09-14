def solve():
    N, M = map(int, input().split())
    board = [input() for _ in range(N)]

    min_changes = float('inf')

    # 모든 8x8 크기의 부분 판 탐색
    for i in range(N - 7):
        for j in range(M - 7):
            # 현재 8x8 부분 판의 시작점 (i, j)

            # Case 1: 시작 칸이 'W'인 경우
            changes_w_start = 0
            for row in range(8):
                for col in range(8):
                    current_char = board[i + row][j + col]
                    
                    # (row + col)의 합이 짝수면 W, 홀수면 B여야 함
                    if (row + col) % 2 == 0:
                        if current_char != 'W':
                            changes_w_start += 1
                    else:
                        if current_char != 'B':
                            changes_w_start += 1
            
            # Case 2: 시작 칸이 'B'인 경우
            changes_b_start = 0
            for row in range(8):
                for col in range(8):
                    current_char = board[i + row][j + col]
                    
                    # (row + col)의 합이 짝수면 B, 홀수면 W여야 함
                    if (row + col) % 2 == 0:
                        if current_char != 'B':
                            changes_b_start += 1
                    else:
                        if current_char != 'W':
                            changes_b_start += 1
            
            # 두 경우 중 더 적게 칠하는 경우를 선택
            min_changes = min(min_changes, changes_w_start, changes_b_start)

    print(min_changes)

# 함수 호출
solve()