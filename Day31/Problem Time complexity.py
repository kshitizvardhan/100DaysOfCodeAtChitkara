# cook your dish here
t=int(input())
for i in range(t):
    X,Y=map(int,input().split())
    if X<=Y:
        print("NO")
    else:
        print("YES")
