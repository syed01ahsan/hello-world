#Syed Ahsan
#1867491


#inputFile = open('C:\\Users\\syed0\Desktop\\inputDates.txt','r')
#outputFile = open('C:\\Users\\syed0\Desktop\\parsedDates.txt','w')

def dates():
    month_list={'january':1,'february':2,'march':3,'april':4,'may':5,'june':6,'july':7,'august':8,'september':9,'october':10,'november':11,'december':12}
    with open('C:\\Users\\syed0\Desktop\\inputDates.txt','r') as input_file:
        list1=input_file.read().splitlines()
    i=0
    list2=[]
    list3=[]
    for k in range(len(list1)):
        if(list1[k].find("/")==-1):
            list3.append(list1[k])
    print("revamped list:",list3)

    while(list3[i]!="-1"):
        string1 = ""
        new_lis=list3[i].split(" ")
        if(new_lis[0].lower() in month_list.keys() and new_lis[1].endswith(',') and
                (int(new_lis[2])>=1000 and int(new_lis[2])<=2020)):
            string1+=str(month_list[new_lis[0].lower()])+'/'+new_lis[1][:-1]+'/'+new_lis[2]+'\n'
            list2.append(string1)
        i+=1
    file2 = open('C:\\Users\\syed0\Desktop\\parsedDates.txt','w')
    file2.writelines(list2)
    file2.close()
dates()
