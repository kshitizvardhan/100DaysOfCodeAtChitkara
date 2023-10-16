n=int(input())
for i in range(n):
    N,M=map(int,input().split())
    if N>M:
        N=N-1
        M=M+1
        if N==M:
            print("YES")
        else:
            print("NO")
    elif N==M:
        print("YES")
    elif N<M:
        N=N+3 
        M=M-1
        if N==M:
            print("YES")
        else:
            print("NO")
    else:
        break
