str="Hello"
count=0
for letter in str:
    if letter=='l':
        count+=1
print(count)     


str="Hello"
count=0
# Using range and function len
for i in range(len(str)):
    if str[i]=='l':
        count+=1
print(count) 
