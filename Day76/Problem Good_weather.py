# cook your dish here
t = int(input())
for _ in range(t):
    days = list(map(int, input().split()))
    sunny_days = 0
    rainy_days = 0
    for day in days:
        if day == 0 :
            rainy_days += 1
        else:
            sunny_days += 1
    if sunny_days > rainy_days:
        print('YES')
    else:
        print('NO')
