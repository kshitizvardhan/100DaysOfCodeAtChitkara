# Strings are immutable like variables it stores references/address of the storage.

s="Kshitiz"
s[0]="B"
print(s)

---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)
Cell In[14], line 2
      1 s="Kshitiz"
----> 2 s[0]="B"
      3 print(s)

TypeError: 'str' object does not support item assignment
