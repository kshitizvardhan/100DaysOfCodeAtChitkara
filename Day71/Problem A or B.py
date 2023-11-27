t = int(input())
for i in range(t):
    X, Y = map(int, input().split())
    A=500
    B=1000
    Option1=(A-X*2)+(B-(X+Y)*4)
    option2=(B-Y*4)+(A-(X+Y)*2)
    print(max(Option1, option2))
