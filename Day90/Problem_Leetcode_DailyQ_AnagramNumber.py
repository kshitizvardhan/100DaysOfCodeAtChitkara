class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False
        letters_count=[0]*26
        for i in range(len(s)):
            letters_count[ord(s[i])-ord("a")]+=1
            letters_count[ord(t[i])-ord("a")]-=1
        for j in letters_count:
            if j!=0:
                return False
        else:
            return True    
        


        
