# cook your dish here
t=int(input())
for _ in range(t):
    x1,y1,x2,y2= map(int,input().split())
    p1= x1-x2
    p2= y1-y2
    if p1<0:
        p1= p1*(-1)
    else:
        p1=p1
    if p2<0:
        p2= p2*(-1)
    else:
        p2=p2
    print(max(p1,p2))    
