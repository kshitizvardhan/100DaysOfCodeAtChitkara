# cook your dish here
t=int(input())
for i in range(t):
    x,y,z=map(int,input().split())
    total_airplanes=10
    totalseats=x*10
    if totalseats>=y:
        y=y*z 
        print(y)
    else:
        y=totalseats*z 
        print(y)
