# cook your dish here
t=int(input())
for i in range(t):
    N,M,K=map(int,input().split())
    maxposs=M*K
    if maxposs>=N:
        print("YES")
    else:
        print("NO")
