# cook your dish here
t=int(input())
for i in range(t):
    a,b,c=map(int,input().split())
    d=a+b 
    e=b+c
    if d%2!=0 or e%2!=0:
        print("YES")
    else:
        print("NO")
