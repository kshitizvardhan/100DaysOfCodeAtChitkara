# Complete the solve function below.
def solve(s):
    newstr=""
    for i in range(len(s)):
        if i==0:
            newstr+=s[i].upper()
        elif s[i-1]==" ":
            newstr+=""+s[i].upper() 
        else:
            newstr+=s[i]    
    return newstr 
