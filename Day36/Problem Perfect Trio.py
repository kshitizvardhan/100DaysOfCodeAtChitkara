# cook your dish here
T=int(input())
for i in range(T):
    A,B,C=map(int,input().split())
    if A+B==C or B+C==A or A+C==B:
        print("YES")
    else:
        print("NO")
