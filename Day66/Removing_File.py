import os
try:
    t=input("Enter file name: ")
    if os.path.exists(t):
        os.remove(t)
        print("File removed successfully!")    
    else:
        print("No Such file exists.")
except Exception as e:
    print("No such file exists, Ensure you type file name Correctly. The error is- ",e)


