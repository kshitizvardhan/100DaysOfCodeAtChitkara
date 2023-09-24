n=int(input("Enter the number items: "))
li=[int(x) for x in input().split()]
ele=int(input("Enter the Number you want to search for: "))
flag=False
for i in range(len(li)):
    if li[i]==ele:
        print("The index number of the ele is",i)
        flag=True
        break
if flag is False:
    print('No Results Found')
