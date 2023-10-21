# cook your dish here
t=int(input())
for i in range(t):
    x,y=map(int,input().split())
    if (x==y and x!=0 and y!=0):
        print("YES")
    else:
        print("NO")
