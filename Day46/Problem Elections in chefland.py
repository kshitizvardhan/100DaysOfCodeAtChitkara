# cook your dish here
t=int(input())
for _ in range(t):
    n,x=map(int,input().split())
    a=[int(x) for x in input().split()]
    eligible=0
    for i in range(0, n):
        if a[i]>=x:
            eligible+=1 
    print(eligible)        
