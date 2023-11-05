# cook your dish here
t=int(input())
for _ in range(t):
    a,b=map(int,input().split())
    add=a+b
    prime=[1,2,3,5,7,11]
    if add in prime:
        print("Alice")
    else:
        print('Bob')
