n=int(input())
for i in range(n):
    x,y=map(int, input().split())
    prize= (10*x) + (90*y)
    print(prize)
