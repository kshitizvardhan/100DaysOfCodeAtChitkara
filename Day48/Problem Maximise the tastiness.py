# cook your dish here
t=int(input())
for i in range(t):
    a,b,c,d=map(int,input().split())
    first1=a+c 
    first2=a+d 
    second1=b+c 
    second2=b+d 
    print(max(first1,first2,second1,second2))
