# cook your dish here
t=int(input())
for i in range(t):
    a,b=[int(q) for q in input().split()]
    req=21-a-b
    if req>10:
        print("-1")
    else:
        print(req)
