# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import permutations
T=input().split()
Permutes= sorted(list(permutations(T[0],int(T[1]))))
Permutes=[''.join(i) for i in Permutes]
for i in Permutes:
    print(i)
