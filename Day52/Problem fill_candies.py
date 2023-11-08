# cook your dish here
for _ in range(int(input())):
    N,K,M=map(int,input().split(' '))
    
    if N%(M*K)==0:
        print((N//(M*K)))
        
    else:
        print((N//(M*K))+1)
