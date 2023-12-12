# Enter your code here. Read input from STDIN. Print output to STDOUT
n=int(input())
li1=set([int(x) for x in input().split()])
m=int(input())
li2=set([int(x) for x in input().split()])
ans= li1.symmetric_difference(li2)
final=sorted(ans)
for i in final:
    print(i)
