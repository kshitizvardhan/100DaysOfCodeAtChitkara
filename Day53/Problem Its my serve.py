# cook your dish here
t=int(input())
for _ in range(t):
    p,q=map(int,input().split())
    serve=p+q
    if serve%4==0 or serve%4==1:
        print("Alice")
    else:
        print("Bob")
