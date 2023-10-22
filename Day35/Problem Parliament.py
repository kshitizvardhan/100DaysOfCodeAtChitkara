# cook your dish here
t=int(input())
for i in range(t):
    N,X=map(int,input().split())
    if N/2<=X:
        print("YES")
    else:
        print("NO")