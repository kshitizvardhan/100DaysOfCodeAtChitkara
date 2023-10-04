n=int(input())
for n in range(n):
    a,b=map(int,input().split())
    if a+b<=6:
        print("NO")
    else:
        print("YES")
