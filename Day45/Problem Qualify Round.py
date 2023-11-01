# cook your dish here
t=int(input())
for i in range(t):
    x,a,b=map(int, input().split())
    a=a*1 
    b=b*2 
    if a+b>=x:
        print("QUALIFY")
    else:
        print("NOTQUALIFY")
