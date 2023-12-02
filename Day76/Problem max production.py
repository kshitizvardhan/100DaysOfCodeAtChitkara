# cook your dish here
t=int(input())
for _ in range(t):
  a,b,c,d=map(int,input().split())
  m1=7*b
  m2=a*c+(7-a)*d
  print(max(m1,m2))
