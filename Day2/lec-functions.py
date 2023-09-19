# Function for Factorial
def fact(a):
    a_fact=1
    for i in range(1,a+1):
        a_fact=a_fact*i
    return a_fact 

# Function for nCr!:

n=int(input())
r=int(input())
n_fact=fact(n)  #Here when the function is called "fact(a)", the a gets the value of n 'input' and stores it in n_fact.
r_fact=fact(r)  # Similarly for r and n-r a gets their value.
n_r_fact=fact(n-r)
ans= n_fact//((r_fact)*(n_r_fact))
print(ans)
