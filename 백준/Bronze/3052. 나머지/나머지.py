
a = [int(input()) for _ in range(10)]

b=[]

for i in range(10):
   b.append(a[i]%42) 

print(len(set(b)))
    