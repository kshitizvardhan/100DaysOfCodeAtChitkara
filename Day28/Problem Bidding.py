n=int(input())
for i in range(n):
    a,b,c=map(int,input().split())
    if a>b and a>c:
        print("ALICE")
    elif b>c and b>a:
        print("BOB")
    elif c>a and c>b:
        print("CHARLIE")
