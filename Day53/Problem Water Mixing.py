# cook your dish here
t=int(input())
for _ in range(t):
    a,b,x,y=map(int,input().split())
    if a==b:
        print("YES")
    elif a<b:
        temp_diff= b-a
        if temp_diff<=x:
            print("YES")
        else:
            print("NO")
    elif a>b:
        temp_diff= a-b
        if temp_diff<=y:
            print("YES")
        else:
            print("NO")
