#Syed Ahsan
#1867491

user = input()
num = 0
count = len(user)-1
result = True
while(num<count):
    if(user[num]==' '):
        num+=1
    elif(user[count]==' '):
        count-=1
    elif(user[num]!=user[count]):
        result = False
        break
    else:
        num+=1
        count-=1
if (result):
    print(user,"is a palindrome")
else:
    print(user, "is not a palindrome")