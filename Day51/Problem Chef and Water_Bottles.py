# cook your dish here
t = int(input())
for _ in range(t):
    N,X,K=map(int,input().split())
    A= K//X
    print(min(N, A))
