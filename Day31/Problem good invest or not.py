# cook your dish here
t=int(input())
for i in range(t):
    X,Y=map(int,input().split())
    Y=Y*2
    if X>=Y:
        print("Yes")
    else:
        print("No")
