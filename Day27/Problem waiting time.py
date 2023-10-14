n=int(input())
for i in range(n):
    K,X=map(int,input().split())
    days= 7*K//1 
    remdays= days-X
    print(remdays)
