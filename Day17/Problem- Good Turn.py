# Chef and Chefina are playing with dice. In one turn, both of them roll their dice at once. They consider a turn to be good if the sum of the numbers on their dice is greater than 
# 6. Given that in a particular turn Chef and Chefina got X and Y on their respective dice, 
# find whether the turn was good.
n=int(input())
for n in range(n):
    a,b=map(int,input().split())
    if a+b<=6:
        print("NO")
    else:
        print("YES")
