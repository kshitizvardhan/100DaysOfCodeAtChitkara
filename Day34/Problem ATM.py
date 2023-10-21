#cook your dish here
X,Y=map(float,input().split())
X=int(X)
if X+0.50<=Y:
    if X%5==0:
        Y=Y-(X+0.50)
        print(float(Y))
    elif X%5!=0:
        print(float(Y))
else:
    print(float(Y))
