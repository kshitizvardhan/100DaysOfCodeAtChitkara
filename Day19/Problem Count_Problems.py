# Our Chef is currently practicing on CodeChef and is a beginner. The count of ‘All Problems’ in the Beginner section is X. Our Chef has already ‘Attempted’ 
# Y problems among them. How many problems are yet ‘Un-attempted’?

x,y=map(int,input().split())
Unattempted= x-y
print(Unattempted)
