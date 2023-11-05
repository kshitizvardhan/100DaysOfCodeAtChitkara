# cook your dish here
t = int(input())
for _ in range(t):
  left,right= map(int,input().split())
  print(min(left-right,right))
