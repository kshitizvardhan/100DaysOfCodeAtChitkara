t=int(input())
for i in range(t):
    li=[int(x) for x in input().split()]
    flag=False
    for j in range(len(li)):
        if li[j]==1:
            flag=True 
    if flag:
        print("OUT")
    else:
        print("IN")
