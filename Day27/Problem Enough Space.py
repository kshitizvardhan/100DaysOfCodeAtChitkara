n=int(input())
for i in range(n):
    N,X,Y=map(int,input().split())
    space= X*1+Y*2
    if N>=space:
        print("YES")
    else:
        print("NO")
