# Chef appeared for a placement test.
# There is a problem worth X points. Chef finds out that the problem has exactly 10 #test # cases. It is known that each test case is worth the same number of points.
# Chef passes N test cases among them. 
# Determine the score Chef will get.


n=int(input())
for i in range(n):
    x,y=map(int,input().split())
    a=x//10
    ans= a*y
    print(ans)
