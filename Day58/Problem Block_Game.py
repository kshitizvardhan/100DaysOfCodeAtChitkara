# cook your dish here
t=int(input())
for i in range(t):
    n=input()
    if n[::-1]==n:
        print("wins")
    else:
        print("loses")
    
