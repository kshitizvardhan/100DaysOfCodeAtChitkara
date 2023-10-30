t=int(input())
for i in range(t):
    n,x=map(int,input().split())
    if n<x:
        print("0")
    elif (n-x)%4==0:
        print((n-x)//4)
    else:
        print((n-x)//4+1)
