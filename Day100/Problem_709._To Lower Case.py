class Solution:
    def toLowerCase(self, s: str) -> str:
        newStr=""
        for i in s:
            newStr+= i.lower()
        return newStr
        
