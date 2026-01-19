import sys

input = sys.stdin.readline

#첫번째 영화 제목 666 시즌2 1666 시즌3 2666

n = int(input())
movie = 0
count = 0

while True:
    movie += 1
    movie_str = str(movie)
    
    if movie_str.find("666") != -1: # if "666" in movie_str:
        count += 1
        
        if count == n:
            break

print(movie_str)


#  로직 요약:
#  1. 숫자를 666부터 무한루프(while True)로 1씩 증가시킨다.
#  2. 숫자를 문자열로 변환해서 '666'이 들어있는지 확인한다.
#  3. 들어있다면 카운트를 올린다.
#  4. 카운트가 N이 되면 그 숫자를 출력하고 종료한다.       
        
    
    
    