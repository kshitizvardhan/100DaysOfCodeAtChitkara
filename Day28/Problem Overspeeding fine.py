n=int(input())
for i in range(n):
    x=int(input())
    if x<=70:
        fine=0
        print(fine)
    elif 70<x<=100:
        fine=500
        print(fine)
    else:
        fine=2000
        print(fine)
