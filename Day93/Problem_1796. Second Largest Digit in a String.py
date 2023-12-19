class Solution:
    def secondHighest(self, s: str) -> int:
        nums=[]
        for i in s:
            if i in ['0','1','2','3','4','5','6','7','8','9']:
                nums.append(int(i))
        num=sorted(list(set(nums)))
        if len(num)<2:
            return -1
        else:
            return num[-2]
            
        

        
