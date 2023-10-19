# cook your dish here
t=int(input())
for i in range(t):
    N,M,X=map(int,input().split())
    total_length= 2*N+M*2 
    cost=total_length*X
    print(cost)
