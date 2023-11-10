# cook your dish here
t=int(input())
for _ in range(t):
    n,a,b = map(int, input().split())
    duration = 0
    for i in range(1, n+1):
        if i%2==0:
            duration += a
        else:
            duration += b
    print(duration)
