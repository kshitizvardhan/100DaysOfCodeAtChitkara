# cook your dish here
t=int(input())
for i in range(t):
    n,x=map(int,input().split())
    bill=n*x 
    length=str(bill)
    if len(length)==5:
        if length[0]!=0:
            print("YES")
        else:
            print("NO")
    else:
        print("NO")
