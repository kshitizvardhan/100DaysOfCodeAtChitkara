# cook your dish here
t=int(input())
for i in range(t):
    n,m=map(int,input().split())
    z = n-n*0.1
    if(z < m):
        print("ONLINE")
    elif(z > m):
        print("DINING")
    else:
        print("EITHER")
