class Solution:
    def numDecodings(self, s: str) -> int:
        if s=="0":
            return 0
        n=len(s)
        counts=[0] * (n+1)
        counts[-1]=1
        counts[-2]=int(s[-1]!="0")
        for i in range(n-2,-1,-1):
            if s[i]=="0":
                counts[i]=0
            else:
                counts[i]=counts[i+1]
                if 1 <= int(s[i:i+2]) <= 26:
                    counts[i]+=counts[i+2]
        return counts[0]
