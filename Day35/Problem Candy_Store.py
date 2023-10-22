# cook your dish here
t=int(input())
for i in range(t):
    X,Y=map(int,input().split())
    if Y>X:
        extra= Y-X
        amt=X*1+(extra*2) 
        print(amt)
    else:
        amt=Y*1 
        print(amt)
    