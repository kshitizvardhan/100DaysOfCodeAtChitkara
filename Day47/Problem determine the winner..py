# cook your dish here
t=int(input())
for _ in range(t):
    pa,pb,qa,qb=map(int,input().split())
    P= max(pa,pb)
    Q= max(qa,qb)
    if P<Q:
        print("P")
    elif P==Q:
        print("TIE")
    else:
        print("Q")
