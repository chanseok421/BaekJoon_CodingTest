max_value = -1
row = 0
col = 0

for i in range(9):
    nums = list(map(int, input().split()))
    for j in range(9):
        if nums[j] > max_value: #비교
            max_value = nums[j] #비교해서 큰값이면 max_value에 저장
            row = i + 1
            col = j + 1
print(max_value)
print(row, col)