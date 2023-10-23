# cook your dish here
t=int(input())
for i in range(t):
    N,M=map(int,input().split())
    N=N*2
    M=M*4
    print(N+M)
