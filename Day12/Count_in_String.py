# Count Vowels, Consonants, Digits, Special Character in a String

def count_in_string(str):
    v,c,d,s=0,0,0,0
    for char in str:
        if (char>='a' and char<='z') or (char>='A' and char<='Z'):
            char=char.lower()
            if (char=='a') or (char=='e') or (char=='i') or (char=='o') or (char=='u'):
                v+=1
            else:
                c+=1
        elif (char>='1' and char<='9'):
            d+=1
        else:
            s+=1
    return v,c,d,s       
str="Abcdefghijklmnopqrstuvwxyz123456789!@#$%^&*"
v,c,d,s= count_in_string(str)
print(v,c,d,s)

>>> 5 21 9 8
