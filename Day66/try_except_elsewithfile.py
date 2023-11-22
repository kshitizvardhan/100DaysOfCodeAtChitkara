try:
    f=open("Filehandling3", "w")
    print("File has been opened.")
except Exception as e:
    print("No Such File found in the directory. Please create a file")    
else:
    f.close()
    print("File Closed")
