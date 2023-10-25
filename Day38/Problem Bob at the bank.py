# cook your dish here
t=int(input())
for i in range(t):
    w,x,y,z=map(int,input().split())
    x=x-y 
    final=w+x*z
    print(final)
