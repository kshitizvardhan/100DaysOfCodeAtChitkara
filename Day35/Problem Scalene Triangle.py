# cook your dish here
t=int(input())
for i in range(t):
    A,B,C=map(int,input().split())
    if A==B:
        print("NO")
    elif B==C:
        print("NO")
    elif C==A:
        print("NO")
    else:
        print("YES")