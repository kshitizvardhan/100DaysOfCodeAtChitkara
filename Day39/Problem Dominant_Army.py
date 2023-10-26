# cook your dish here
t=int(input())
for i in range(t):
    Na,Nb,Nc=map(int,input().split())
    if Na> Nb+Nc or Nb>Na+Nc or Nc>Na+Nb:
        print("YES")
    else:
        print("NO")
