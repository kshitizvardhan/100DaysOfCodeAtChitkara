# A blood drive aims to collect N number of blood donations.
# The drive has collected X donations so far. Find the remaining number of donations #needed to reach the target.


n=int(input())
for i in range(n):
    x,y=map(int,input().split())
    remain=x-y
    print(remain)
