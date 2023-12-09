def wrap(string, max_width):
    li1=[]
    newstr=""
    for i in range(len(string)):
        if i!=0 and i%max_width==0:
            li1.append(newstr)
            newstr+= '\n'+ string[i]
        else:
            newstr+=string[i]  
    li1.append(newstr)       
    wrapstr=''.join(li1)  
    return newstr
