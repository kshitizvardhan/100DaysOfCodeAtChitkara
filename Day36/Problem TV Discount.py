# cook your dish here
t=int(input())
for i in range(t):
    A,B,C,D=map(int,input().split())
    cost1=A-C
    cost2=B-D
    if cost1==cost2:
        print("ANY")
    elif cost1<cost2:
        print("FIRST")
    else:
        print("SECOND")
