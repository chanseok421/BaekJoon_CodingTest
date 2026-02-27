import sys

# 빠르게 입력받기 위해 sys.stdin.readline 사용
input = sys.stdin.readline

def solve():
    N = int(input())
    
    # 인사를 한 사람을 기록할 집합 (중복 방지)
    entered_users = set()
    count = 0
    
    for _ in range(N):
        log = input().strip() # 개행문자 제거
        
        if log == "ENTER":
            # 새로운 입장이 발생했으므로 집합 초기화
            entered_users.clear()
        else:
            # 현재 구간에서 처음 말하는 경우에만 카운트
            if log not in entered_users:
                count += 1
                entered_users.add(log)
    
    print(count)

if __name__ == "__main__":
    solve()