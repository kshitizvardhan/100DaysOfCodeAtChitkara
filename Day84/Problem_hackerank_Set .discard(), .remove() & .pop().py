n = int(input())
s = set(map(int, input().split()))
for i in range(int(input())):
    li1=input().split()
    if li1[0]=="remove":
        s.remove(int(li1[1]))
    elif li1[0]=="discard":
        s.discard(int(li1[1]))
    elif li1[0]=="pop":
        s.pop()
sum=0
for i in s:
    sum+=i
print(sum)
