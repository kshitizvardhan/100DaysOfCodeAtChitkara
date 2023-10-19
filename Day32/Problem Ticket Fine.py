# cook your dish here
t=int(input())
for i in range(t):
    X,P,Q=map(int,input().split())
    fine=X*(P-Q)
    print(fine)
