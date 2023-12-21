class Solution:
    def maxWidthOfVerticalArea(self, points: List[List[int]]) -> int:
        Points=sorted(points)
        max_width=0
        for i in range(1,len(Points)):
            max_width=max(max_width, Points[i][0] - Points[i - 1][0])
        return max_width
