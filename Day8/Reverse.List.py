Method-1 Through Swapping

def reverse_l(li):
    length=len(li)
    for i in range(length//2):
        li[i],li[length-i-1]=li[length-i-1],li[i]
        
li=[1,2,3,4,5,6]
reverse_l(li)
print(li)

Method-2 Through Indexing

li=[1,2,3,4,5,6]
li=li[::-1]
print(li)
