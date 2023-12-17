class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = ((i.lower()) for i in s if i.isalnum())
        s="".join(s)
        rev= s[::-1]
        if rev==s:
            return True
        else:
            return False
