# cook your dish here
t=int(input())
for i in range(t):
    X,Y=map(int,input().split())
    cost2= X*3
    cost3= Y*2 
    if cost3>cost2:
        print(cost2)
    else:
        print(cost3)
