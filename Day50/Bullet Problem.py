t = int(input())
for _ in range(t):
    x,y,z = map(int,input().split())
    k = y//x
    m = z-k
    
    if m<=0:
        print(0)
    elif m>0:
        print(m)
    
