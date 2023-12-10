# Enter your code here. Read input from STDIN. Print output to STDOUT
t=int(input())
country=[] #removing duplicates in list by converting list to a set
for i in range(t):
    s=input()
    country.append(s)
print(len(set(country)))
