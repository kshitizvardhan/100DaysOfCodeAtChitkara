n=int(input())
neigh=20
if(1<=n<=405):
    for i in range(n):
        x, y = [int(x) for x in input().split()]
        c=x//y
        if (1<=x<=100 and 1<=y<=5 ):
            if(c<=20):
                print(c)
            else:
                c=20
                print(c)
