i=int(input())
n=i
rev=0
while i>0:
    rev=(rev*10)+(i%10)
    i=i//10
if(n==rev):
    print("true")
else:
    print("false")
