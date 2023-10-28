# cook your dish here
t=int(input())
for i in range(t):
    x,y=map(int,input().split())
    coins=x*y 
    maxnum=coins//100
    print(maxnum)    
