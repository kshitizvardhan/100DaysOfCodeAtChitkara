# cook your dish here
t=int(input())
for i in range(t):
    hidden=list(input())
    guess=list(input())
    M=""
    for ele in range(len(hidden)):
        if hidden[ele]==guess[ele]:
            M+="G"
        else:
            M+="B"
    print(M)            
