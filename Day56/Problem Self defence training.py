# cook your dish here
t=int(input())
for i in range(t):
    n=int(input())
    li=list(map(int,input().split()))
    count=0
    for i in li:
        if i>=10 and i<=60:
            count+=1 
    print(count)        
