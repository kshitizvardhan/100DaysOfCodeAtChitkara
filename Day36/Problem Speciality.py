# cook your dish here
t=int(input())
for i in range(t):
    X,Y,Z=map(int, input().split())
    if X>Y and X>Z:
        print("SETTER")
    elif Y>Z and Y>X:
        print("TESTER")
    else:
        print("EDITORIALIST")
