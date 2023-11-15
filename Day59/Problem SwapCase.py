def swap_case(s):
    new = ""
    for i in range(len(s)):
        if s[i].upper() == s[i]:
            new += s[i].lower()
        else:
            new += s[i].upper()
    return new
        
if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)
