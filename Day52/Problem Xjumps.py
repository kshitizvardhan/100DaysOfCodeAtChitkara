# cook your dish here
t=int(input())
for i in range(t):
    x,y=map(int,input().split())
    if y<=x:
        print((x//y)+(x%y))
    elif x<y:
        print(-(x//y)+(x%y))
    
        
