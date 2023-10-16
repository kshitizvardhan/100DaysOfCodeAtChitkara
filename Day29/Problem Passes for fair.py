t=int(input())
for i in range(t):
    N,K=map(int,input().split())
    if N<K:
        print("YES")
    elif N>=K:
        print("NO")
