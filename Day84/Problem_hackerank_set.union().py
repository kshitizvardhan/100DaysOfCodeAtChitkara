n=int(input())
s=set([int(x) for x in input().split()])
n1=int(input())
s1=set([int(x) for x in input().split()])
ans=s.union(s1)
print(len(set(ans)))   