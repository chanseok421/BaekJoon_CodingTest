while True:
    n = int(input())
    
    if n == -1:
        break
    
    arr = []
    for i in range(1, n):
        if n % i == 0:
            arr.append(i)
    
    if sum(arr) == n:
        print(f"{n} = {' + '.join(map(str, arr))}")
    else:
        print(f"{n} is NOT perfect.")
        

    
#     if sum(arr) == n:
#         print(f"{n} = {' + '.join(map(str, arr))}")
#     else:
#         print(f"{n} is NOT perfect.")
                
    
#     1. f"{n} = ..."
# 이건 f-string, 즉 문자열 안에 변수 값을 바로 넣는 방법

# 예를 들어 n = 28이면 → "28 = ..." 이렇게 시작하는 문자열이 됨

# 2. map(str, divisors)
# divisors 리스트 안에는 숫자가 들어있지?

# 그걸 모두 문자열(str) 로 바꿔주는 과정이야

# 예: [1, 2, 4, 7, 14] → ["1", "2", "4", "7", "14"]

# 3. ' + '.join(...)
# 이건 문자열을 합칠 때 사용하는 메서드

# ' + '를 사이에 넣어서 리스트를 이어줌

# 결과: "1 + 2 + 4 + 7 + 14"
        
    
    
    