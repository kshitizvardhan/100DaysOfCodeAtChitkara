# cook your dish here
t=int(input())
for i in range(t):
    x,y,m=map(int,input().split())
    totalrent=x*m 
    if totalrent<y:
        print("YES")
    else:
        print("NO")
