# cook your dish here
t=int(input())
for i in range(t):
    r1,r2,r3=map(int,input().split())
    if r1 > r2+r3 or r2> r1+r3 or r3>r1+r2:
        print("YES")
    else:
        print("NO")
