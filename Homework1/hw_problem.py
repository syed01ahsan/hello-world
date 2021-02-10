#Syed Ahsan
#1867491

print('Birthday Calculator')
print('Current day')
curr_month= int(input('Month: '))
curr_day= int(input('Day: '))
curr_year= int(input('Year: '))
print('Birthday')
user_month= int(input('Month: '))
user_day= int(input('Day: '))
user_year= int(input('Year: '))
years = curr_year-user_year-1
if(user_month<curr_month):
    years+=1
elif(curr_month==user_month):
    if(user_day<curr_day):
        years+=1
if(curr_month==user_month and curr_day==user_day):
    print('Happy Birthay')
print('You are '+str(years)+" years old.")



