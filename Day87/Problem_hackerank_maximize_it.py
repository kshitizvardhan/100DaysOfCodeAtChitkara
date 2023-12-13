# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import product
k, m = map(int, input().split())
high=[]
for _ in range(k):
    li=[int(x) for x in input().split()]
    li.pop(0)
    high.append((li))
sumMax=0
for i in product(*high):
    sum1= sum(x**2 for x in i)
    maxEqn= sum1 % m
    if maxEqn>sumMax:
        sumMax=maxEqn
        
print(sumMax)


