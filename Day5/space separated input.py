# space separated input of list in integer
str=(input())
str_split= str.split(' ')
print(str_split)
li=[]
for ele in str_split:
    li.append(int(ele))
print(li) 
