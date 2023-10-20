# cook your dish here
t=int(input())
for i in range(t):
    X,Y=map(int,input().split())
    if X<=Y<=X+200:
        print("YES")
    else:
        print("NO")
