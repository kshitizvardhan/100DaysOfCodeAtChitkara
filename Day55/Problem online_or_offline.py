# cook your dish here
t=int(input())
for i in range(t):
    n,m=map(int,input().split())
    n=n-(n*10)//100
    if n==m:
        print("EITHER")
    elif n>m:
        print("DINING")
    elif n<m:
        print("ONLINE")
