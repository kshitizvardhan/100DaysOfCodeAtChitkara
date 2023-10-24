# cook your dish here
T=[int(x) for x in input().split()]
prblm=0
for i in range(len(T)):
    if T[i]>=10:
        prblm+=1 
print(prblm)                
