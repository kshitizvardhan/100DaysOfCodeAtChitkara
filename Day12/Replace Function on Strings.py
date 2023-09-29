# Replace Function

a="My name is Kshitiz"
b=a.replace("Kshitiz", "ABC")
print(b)
# As strings are immutable, the original variable 'a' is not changed rather a new string is created.
print(a)

a="My name is Kshitiz Kshitiz Kshitiz Kshitiz"
b=a.replace("Kshitiz", "ABC",3)
print(b)

