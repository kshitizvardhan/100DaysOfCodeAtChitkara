li=[[1,2,3,4],[5,6,7,8],[9,10,11,12]]
n=3
m=4
for rows in range(n):
    for cols in range(m):
        print(li[rows][cols], end=" ")
    print()    



# In case of Jagged lists
li=[[1,2,3,4],[5,6],[9,10,11,12]]
n=3
for rows in li:
    for ele in rows:
        print(ele, end=" ")
    print()
