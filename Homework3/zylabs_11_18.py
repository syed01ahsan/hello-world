#Syed Ahsan
#1867491

user = input()
list_values = [int(num) for num in user.split()
if int(num) > -1]
list_values.sort()
for value in list_values:
    print(value, end = ' ')