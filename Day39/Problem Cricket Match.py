# cook your dish here
t=int(input())
for i in range(t):
    n,m=map(int,input().split())
    totalballs=m*6
    maxruns= totalballs*6
    if maxruns>=n:
        print("YES")
    else:
        print("NO")
