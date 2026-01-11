for _ in range(3):
    n = int(input())

    total = 0

    for i in range(n):
        i = int(input())
        total += i
        
    if total == 0:
        print('0')

    elif total < 0:
        print('-')
        
    elif total > 0:
        print('+')


