# cook your dish here
t=int(input())
for i in range(t):
    X,Y=map(int,input().split())
    need=X*3
    if need<=Y:
        print("YES")
    else:
        print("NO")
