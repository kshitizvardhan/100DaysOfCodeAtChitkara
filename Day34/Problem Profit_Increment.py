# cook your dish here
t=int(input())
for i in range(t):
    X,Y=map(int,input().split())
    newsell= X+(X*10//100)
    BuyPrice=X-Y
    newprofit= newsell-BuyPrice
    print(newprofit)
