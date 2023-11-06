# cook your dish here
t=int(input())
for i in range(t):
    x,y=map(int,input().split())
    z=y-x
    if z==0:
        print(0)
    elif z <= 8:
        print(1)
    else:
        d=z//8
        if z % 8==0:
            print(d)
        else:
            print(d+1)
