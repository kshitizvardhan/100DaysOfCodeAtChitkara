# cook your dish here
T=int(input())
for i in range(T):
    x,y=map(int,input().split())
    x=x*15 
    y=y*2
    if x>=y:
        print("YES")
    else:
        print("NO")
