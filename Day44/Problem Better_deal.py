# cook your dish here
t=int(input())
for i in range(t):
    a,b=map(int,input().split())
    A=100*a/100
    p1=100-A
    B=200*b/100
    p2=200-B
    if p1>p2:
        print("SECOND")
    elif p1==p2:
        print("BOTH")
    else:
        print("FIRST")
