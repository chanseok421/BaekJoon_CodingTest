N, M = map(int, input().split()) #N은 행 개수 , M은 열 개수
A, B = [], [] #두 행렬을 저장할 리스트 준비
 
for _ in range(N):
    row = list(map(int, input().split()))
    A.append(row)
 
for _ in range(N):
    row = list(map(int, input().split()))
    B.append(row)
 
for row in range(N):
    for col in range(M):
        print(A[row][col] + B[row][col], end =' ')
    print() #한줄 끝나면 줄바꿈
    