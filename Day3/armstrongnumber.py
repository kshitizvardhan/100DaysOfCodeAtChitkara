num = int(input())
sum = 0
f = num
while f > 0:
   a = f % 10
   sum = sum + (a ** 3)
   f=(f//10)
if num == sum:
   print("true")
else:
   print("false")
