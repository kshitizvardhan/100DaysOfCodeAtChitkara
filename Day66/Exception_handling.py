a=int(input("Enter the number: "))
b=int(input("Enter the number: "))
try:
    print(a/b)
    c=int(input("Enter the number: "))
    print(c)
except ZeroDivisionError as e: # Here the Error is specified to only print this when this particular error occurs 
    print("Cannot divide by zero. The error is-",e)
except ValueError as e: # Here the Error is specified to only print this when this particular error occurs 
    print("Invalid input. The error is-",e)
except Exception as e: # Here for the safe side, this is used so that we can print for the other errors. 
    print("SOMETHING GONE WRONG")    
finally:
    print("Code finishes") 
