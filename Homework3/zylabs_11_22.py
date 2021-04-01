#Syed Ahsan
#1867491

user = input().split()
for word in user:
    count = 0
    for w in user:
        if w == word:
            count += 1
    print(word, count)