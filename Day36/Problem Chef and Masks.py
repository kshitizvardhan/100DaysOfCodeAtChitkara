# cook your dish here
t=int(input())
for i in range(t):
    X,Y=map(int,input().split())
    X=X*100 
    Y=Y*10
    if X<Y:
        print("DISPOSABLE")
    elif X>Y:
        print("CLOTH")
    elif X==Y:
        print("CLOTH")
    
