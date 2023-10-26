# cook your dish here
t=int(input())
for i in range(t):
    w,x,y,z=map(int,input().split())
    capleft=x-w
    filled=z*y
    if capleft==filled:
        print("filled")
    elif capleft<filled:
        print("overflow")
    else:
        print("unfilled")
