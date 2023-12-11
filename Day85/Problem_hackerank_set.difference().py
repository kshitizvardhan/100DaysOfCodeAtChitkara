# Enter your code here. Read input from STDIN. Print output to STDOUT
n=int(input())
s1=set([int(x) for x in input().split()])
n1=int(input())
s2=set([int(x) for x in input().split()])
ans= s1.difference(s2)
print(len(set(ans)))
