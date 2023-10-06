# In Chefland, everyone who earns strictly more than  Y rupees per year, has to pay a tax to Chef. Chef has allowed a special scheme where you can invest any amount of money and claim exemption for it.
# You have earned X (>) (X>Y) rupees this year. Find the minimum amount of money you have to invest so that you don't have to pay taxes this year.

n=int(input())
for i in range(n):
    x,y=map(int,input().split())
    invest=x-y
    print(invest)
