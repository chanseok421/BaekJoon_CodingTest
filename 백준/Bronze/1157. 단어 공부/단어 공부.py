word = input().upper() # Mississipi
word_list = list(set(word)) # ['P', 'M', 'S', 'I']
cnt = []
 
for i in word_list:
    cnt.append(word.count(i)) # cnt = [4, 1, 1, 4]
 
 
max_count = max(cnt)
if cnt.count(max_count) > 1:
    print("?")
else:
    print(word_list[cnt.index(max_count)])