# cook your dish here
t=int(input())
for _ in range(t):
    n=int(input())
    if 1<=n<=10:
        print("Lower Double")
    elif 11<=n<=15:
        print("Lower Single")
    elif 16<=n<=25:
        print("Upper Double")
    else:
        print("Upper Single")
        
