# cook your dish here
t=int(input())
for i in range(t):
    x, y, d = map(int,input().split())
    if abs(x - y) <= d:
        print("Yes")
    else:
        print("No")
