n=int(input())
for i in range(n):
    x,y,z=map(int,input().split())
    if x+y==z:
        print("YES")
    else:
        print("NO")
