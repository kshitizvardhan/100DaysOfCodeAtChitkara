n=int(input())
for i in range(n):
    x,y=map(int, input().split())
    check=x+y 
    if check%2==0:
        print("YES")
    else:
        print("NO")
