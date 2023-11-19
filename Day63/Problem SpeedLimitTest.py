# cook your dish here
t=int(input())
for _ in range(t):
    a, b, c, d=map(int, input ().split())
    e=a/b 
    f=c/d 
    if e==f :
        print("Equal")
    elif e<f :
        print("Bob")
    else :
        print("Alice")
