t=int(input())
for i in range(t):
    try:
        a,b=map(int,input().split())
        try:
            ans= a//b
            print(ans) 
        except Exception as e:
            print("Error Code:",e)        
    except Exception as e:
        print("Error Code:",e)
