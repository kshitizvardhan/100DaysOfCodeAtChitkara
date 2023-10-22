# cook your dish here
t=int(input())
for i in range(t):
    A,B,C=map(int,input().split())
    if A>=10 and B>=10 and C>=10:
        sum=A+B+C 
        if sum>=100:
            print("PASS")
        else:
            print("FAIL")
    else:
        print("FAIL")