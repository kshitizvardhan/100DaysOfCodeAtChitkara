# cook your dish here
t=int(input())
for _ in range(t):
    n=int(input())
    if n%4==0:
        cars=n//4
    else:
        cars=(n//4) + 1 
    print(cars)
    
