n=int(input())
for i in range(n):
    x=[int(x) for x in input().split()]
    x.sort()
    print(x[1])
