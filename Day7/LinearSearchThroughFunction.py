n=int(input("Enter the number items: "))
li=[int(x) for x in input().split()]
ele=int(input("Enter the Number you want to search for: "))
def linearSearch(li,ele):
    for i in range(len(li)):
        if li[i]==ele: 
            return i
    return "No Results Found"    
index=linearSearch(li,ele)
print(index)
