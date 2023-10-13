n=int(input())
for i in range(n):
    x,y,z=map(int,input().split())
    totalcred= 4*x + 2*y + 0*z
    print(totalcred)
