def replace(str, char1, char2):
    newStr=""
    for char in str:
        if (char==char1):
            newStr+=char2
        else:
            newStr+=char
    return newStr    
str="abbbbcd"
str=replace(str,'b','a')
print(str)

>>> "aaaaacd"
