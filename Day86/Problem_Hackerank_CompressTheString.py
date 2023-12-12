# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import groupby   # importing groupby() function of itertools. as the problem statement specified.
str=input()
for k,g in groupby(str):
    Occurences=list(g)
    print((len(Occurences), int(k)),end=" ")
    
