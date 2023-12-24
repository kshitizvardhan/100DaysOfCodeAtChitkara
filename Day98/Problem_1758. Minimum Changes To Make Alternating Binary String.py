class Solution:
    def minOperations(self, s: str) -> int:
        zero_count= 0
        one_count= 0
        for i in range(len(s)):
            if i%2==0:
                if s[i]=="0":
                    one_count+=1
                else:
                    zero_count+=1
            else:
                if s[i]=="1":
                    one_count+=1
                else:
                    zero_count+=1
        return min(zero_count, one_count)
