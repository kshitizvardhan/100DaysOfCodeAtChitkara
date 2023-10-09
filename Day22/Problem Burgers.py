n=int(input())
for i in range(n):
    x,y=map(int,input().split())
    if x>=y:
        a=x-y
        ans=x-a
        print(ans)
    else:
        a=y-x
        ans=y-a
        print(ans)
