class Solution:
    def maxProductDifference(self, nums: List[int]) -> int:
        N=sorted(nums)
        Pair1 = N[-1] * N[-2]
        Pair2 = N[0] * N[1]
        return Pair1 - Pair2
