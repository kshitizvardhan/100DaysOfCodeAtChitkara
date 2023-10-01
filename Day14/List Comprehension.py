# List Comprehension

li=[1,2,3,4]
li_square=[]
for ele in li:
    li_square.append(ele**2)
print(li_square)  

# But through List comprehension the code can be reduced to a single line.
li_square_c=[ele**2 for ele in li]
print(li_square_c)
>>>
[1, 4, 9, 16]
[1, 4, 9, 16]


# Similarly
li_even_square=[ele**2 for ele in li if ele%2==0]
print(li_even_square)
>>>
[4, 16]


# Elements which are multiple of 2 and 3
li=[1,2,3,4,5,6]
li_multiple_2_3=[ele for ele in li if ele%2==0 if ele%3==0]
print(li_multiple_2_3)
>>>
[6]


# Common ele List of li_1 and li_2
li_1=[1,2,3,4,5]
li_2=[2,4,6,7]
li_common=[ele1 for ele1 in li_1 for ele2 in li_2 if ele1==ele2]
print(li_common)
>>>
[2, 4]


# Using If-else in List Comprehension
li=[1,2,3,4,5]
new_li=[ele**2 if ele%2==0 else ele for ele in li]
print(new_li)
>>>
[1, 4, 3, 16, 5]


s='abcdefgh'
li=[ele for ele in s]
print(li)
>>>
['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
