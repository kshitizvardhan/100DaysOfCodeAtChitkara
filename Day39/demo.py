from calc import add

def func1():
    add() # here then the __name__ prints the 'calc', as the module not running here on demo.py
    print("from func1")

func1() 