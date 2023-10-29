# cook your dish here
t=int(input())
for i in range(t):
    a,b,x,y=map(int,input().split())
    A=a*b
    power=x*y
    if power>=A:
        print("YES")
    else:
        print("NO")
