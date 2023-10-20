# cook your dish here
t=int(input())
for i in range(t):
    X,Y=map(int,input().split())
    X*=5
    if X>=Y:
        print("YES")
    else:
        print("NO")
