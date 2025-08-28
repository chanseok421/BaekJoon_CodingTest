import sys

s = sys.stdin.readline().strip()
n = len(s)
max_len = 0


for i in range(n):

    for j in range(i + 1, n):

        sub = s[i:j+1]
        sub_len = len(sub)
        
   
        if sub_len % 2 == 0:
            half_len = sub_len // 2
           
            front_sum = 0
            back_sum = 0
            
            for k in range(half_len):
                front_sum += int(sub[k])
                back_sum += int(sub[half_len + k])
            
          
            if front_sum == back_sum:
                if sub_len > max_len:
                    max_len = sub_len

print(max_len)