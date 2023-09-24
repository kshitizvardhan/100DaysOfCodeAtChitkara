-----------# Immutable Concept------------

x=3
a=4
print(id(a))
print(id(x))
a=x
a=5
print(id(a))
# --> 140703750198152
# --> 140703750198120
# --> 140703750198184

------------# Mutable Concept---------------

li=[1,2,3,4]
li2=li
li2[1]=4
print(id(li))
print(id(li2))
print(li)
# --> 2591247759744
# --> 2591247759744
# --> [1, 4, 3, 4]
​
