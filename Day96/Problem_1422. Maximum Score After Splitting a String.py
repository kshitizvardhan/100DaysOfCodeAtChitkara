class Solution:
    def maxScore(self, s: str) -> int:
        Max_score=zero=0
        one=s.count("1")
        for i in range(len(s)-1):
            if s[i]=="1":
                one-=1
            else:
                zero+=1
            Max_score=max(Max_score, zero+one)
        return Max_score 
