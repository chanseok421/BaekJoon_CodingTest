word = input()
alpabet = 'abcdefghijklmnopqrstuvwxyz' # 알파벳 문자열 준비

for ch in alpabet:
    print(word.find(ch), end =' ')
    
        
# 문자열.find(찾을문자)
# 🔹 기능
# 문자열에서 찾을 문자가 처음 나오는 위치를 반환

# 찾는 문자가 없다면 -1을 반환