# 2D List using List Comprehension

li=['abcd','efgh','ijkl','mnop']
li_2d=[[s for s in ele] for ele in li]
print(li_2d)

>>>
[['a', 'b', 'c', 'd'], ['e', 'f', 'g', 'h'], ['i', 'j', 'k', 'l'], ['m', 'n', 'o', 'p']]
