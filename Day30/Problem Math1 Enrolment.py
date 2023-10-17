t=int(input())
for i in range(t):
    X,Y=map(int,input().split())
    if Y>=X:
        minseats=Y-X
        print(minseats)
    elif Y<X:
        minseats=0
        print(minseats)
        
