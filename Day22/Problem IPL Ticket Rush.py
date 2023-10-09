# cook your dish here
n=int(input())
for i in range(n):
    x,y=map(int,input().split())
    if x>=y:
        a=x-y
        print(a)
    else:
        a=0
        print(a)
