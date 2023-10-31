# cook your dish here
t=int(input())
for i in range(t):
    a,b,c=map(int,input().split())
    if b>=c and b>=a:
        print("YES")
    else:
        print("NO")
