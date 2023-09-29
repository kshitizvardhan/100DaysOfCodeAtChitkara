# Find Function finds the substring

a="My name is Kshitiz"
b=a.find('is')
print(b)

a="My name is Kshitiz"
b=a.find('nae')
print(b)

# if the substring not present then function returns -1

a="My name is Kshitiz Kshitiz "
b=a.find('Kshitiz')
print(b)

a="My name is Kshitiz Kshitiz "
b=a.find('Kshitiz',15,26)
print(b)
