# Was Able to only pass 140 / 196 testcases, with this solution.

class Solution:
    def largestOddNumber(self, num: str) -> str:
        number=int(num)
        List=[]
        if number%2!=0:
            List.append(number)
        for i in num:
            if int(i)%2!=0:
                List.append(int(i))
        if List==[]:
            return ""
        else:
            return str(max(List))

# So after analyzing error, i found that my approach was wrong, i had to start iterating from the last of the string and check the last digit whether even or odd, and therefore return the largestOddNumber String.
# Here is the solution which passed all the testcases.
class Solution:
    def largestOddNumber(self, num: str) -> str:
        length=len(num)
        for i in range(length-1,-1,-1):
            if num[i] in {'1', '3', '5', '7', '9'}:
                return num[:i + 1]
        else:
            return ""

        
        
        
