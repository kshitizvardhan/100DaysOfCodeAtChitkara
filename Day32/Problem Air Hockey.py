# cook your dish here
t=int(input())
for i in range(t):
    A,B=map(int,input().split())
    req=7
    if A>=B:
        minimum= req-A
        print(minimum)
    elif A<B:
        minimum= req-B
        print(minimum)
