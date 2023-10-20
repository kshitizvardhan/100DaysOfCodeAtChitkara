# cook your dish here
t=int(input())
for i in range(t):
    X,Y=map(int,input().split())
    if X<Y:
        print("first")
    elif X>Y:
        print("second")
    else:
        print("any")
