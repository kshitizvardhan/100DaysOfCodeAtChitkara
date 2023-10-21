# cook your dish here
n=int(input())
for n in range(n):
    up,down=map(int,input().split())
    if up>down:
        change=up-down
        print(change)
    else:
        change=down-up
        print(change)
