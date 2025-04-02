dial = ['ABC', 'DEF', 'GHI', 'JKL', 'MNO', 'PQRS', 'TUV', 'WXYZ']
word = input()
total_time = 0

for char in word:  # 입력된 단어의 각 알파벳에 대해
    for i in range(len(dial)):  # dial 리스트를 돌면서
        if char in dial[i]:  # 해당 알파벳이 dial[i] 안에 있다면
            total_time += i + 3  # 인덱스 + 3초 (2번 다이얼은 3초 걸림)
            break  # 찾았으면 더 이상 찾을 필요 없으니 break

print(total_time)