# Function to check whether number is prime or not.
def isPrime(n):
    for d in range(2,n):
        if n%d==0:
            break
    else:
        return True
    return False


#Printing prime numbers from 2 to N

def primeFrom2toN(n):
    for i in range(2,n+1):
        #Check if i is prime, incase it is we print it.
        is_i_prime=isPrime(i)
        if (is_i_prime):
            print(i)
        
