# cook your dish here
t=int(int(input()))
for i in range(t):
    X,Y=map(int, input().split())
    if X==Y:
        print("ANY")
    elif X<Y:
        print("REPAIR")
    else:
        print("NEW PHONE")
