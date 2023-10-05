n,m=map(int,input().split()) # where n-rows and m-columns
li=[[int(j) for j in input().split()] for i in range(n)]
print(li)

>>>
3 4
1 2 3 4
5 6 7 8
9 10 11 12

[[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]

# 2nd Method- input in single line
n,m=map(int,input().split()) # where n-rows and m-columns
b=input().split()
arr=[[int(b[m*i+j]) for j in range(m)] for i in range(n)]
print("\n")
print(arr)

>>>
3 4
1 2 3 4 5 6 7 8 9 10 11 12

[[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]
