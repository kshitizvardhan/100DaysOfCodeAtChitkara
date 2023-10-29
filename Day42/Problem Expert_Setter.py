# cook your dish here
t=int(input())
for i in range(t):
    x,y=map(int,input().split())
    x=x*50/100
    if y>=x:
        print("YES")
    else:
        print("NO")
