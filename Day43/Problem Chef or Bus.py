# cook your dish here
for i in range(int(input())):
    x, y = map(int, input().split())
    if x<y:
        print("bike")
    elif x>y:
        print("car")
    else:
        print("same")
