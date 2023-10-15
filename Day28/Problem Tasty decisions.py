n=int(input())
for i in range(n):
    x,y=map(int,input().split())
    chocolate= x*2
    candy=y*5
    if candy>chocolate:
        print("CANDY")
    elif candy==chocolate:
        print("EITHER")
    else:
        print("CHOCOLATE")
