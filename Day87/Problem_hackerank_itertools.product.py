# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import product
a=[int(x) for x in input().split()]
b=[int(x) for x in input().split()]
AXB=[]
AXB.append(a) 
AXB.append(b) 
ans=list(product(*AXB))
for i in ans:
    print(i, end=" ")
