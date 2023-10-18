# cook your dish here
t=int(input())
for i in range(t):
    N,X,K=map(int,input().split())
    total=N*X 
    if total<=K:
        print("YES")
    else:
        print("NO")
