# cook your dish here
t=int(input())
for i in range(t):
    B1,B2,B3=map(int,input().split())
    if B1 ==0 and B2==0:
        print("Water filling time")
    elif B1==0 and B3==0:
        print("Water filling time")
    elif B2==0 and B3==0:
        print("Water filling time")
    else:
        print("Not now")
