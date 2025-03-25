n = int(input())

bar = [int(input()) for _ in range(n)]

result = []
max_height = 0 #지금 까지 봤던 막대 중 가장 높은것

# for i in range(0, n):
#     if bar[-1] < bar[i]:
#         result.append(bar.pop()) 논리적 오류 생김

while bar: #막대기가 bar안에 있을때까지 참
    height = bar.pop() #맨 오른쪽 막대 하나 꺼내기
    if height > max_height: # 지금까지 본 것보다 높으면
        result.append(height) # 이 막대는 보이는 것 -> 저장
        max_height = height #현재 최대 높이 갱신


print(len(result))