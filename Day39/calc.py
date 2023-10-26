def add():
    print("result 1 is", __name__) # here the name __name__ prints '__main__', as this module is running here itself.
def sub():
    print("result 2 is")

def main():
    add()  # calling both these functions through one function main()
    sub()        

if __name__=="__main__": 
    main()    