#According to a recent survey, Biryani is the most ordered food. Chef wants to learn how to make world-class Biryani from a MasterChef. Chef will be required to attend the MasterChef's classes for 
# X weeks, and the cost of classes per week is Y coins. 
# What is the total amount of money that Chef will have to pay?
n=int(input())
for i in range(n):
    x,y=map(int,input().split())
    to_pay= x*y
    print(to_pay)
