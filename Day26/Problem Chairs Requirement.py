n=int(input())
for i in range(n):
    x,y=map(int,input().split())
    if x>=y:
        ans=x-y
        print(ans)
    else:
        print("0")
