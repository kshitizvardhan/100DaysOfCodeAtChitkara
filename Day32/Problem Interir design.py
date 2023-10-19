# cook your dish here
t=int(input())
for i in range(t):
    A,B,C,D=map(int,input().split())
    if A+B > C+D:
        print(C+D)
    else:
        print(A+B)
