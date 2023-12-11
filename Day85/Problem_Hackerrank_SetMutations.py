# Enter your code here. Read input from STDIN. Print output to STDOUT
n=int(input())
s1=set([int(x) for x in input().split()])
for i in range(int(input())):
    li1=input().split()
    s2=set([int(x) for x in input().split()])
    if li1[0]=="intersection_update":
        s1.intersection_update(s2)
    elif li1[0]=="update":
        s1.update(s2)
    elif li1[0]=="difference_update":
        s1.difference_update(s2)
    elif li1[0]=="symmetric_difference_update":
        s1.symmetric_difference_update(s2)
sum=0
for j in s1:
    sum+=j
print(sum)
