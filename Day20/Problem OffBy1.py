# You just bought a new calculator, but it seems to have a small problem: all its #results have an extra 1 appended to the end.
#For example, if you ask it for 3 + 5, it'll print 81, and 4 + 12 will result in 161.

#Given A and B, can you predict what the calculator will print when you ask it for A+B?


x,y=map(int,input().split())
sum=x+y
prob=str(sum)
c="1"
ans= prob+c
print(ans)
