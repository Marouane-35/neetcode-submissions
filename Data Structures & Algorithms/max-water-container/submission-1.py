class Solution:
    def maxArea(self, heights: List[int]) -> int:
        Max=0
        i=0
        j=len(heights)-1
        while i<j :
            Max=max((j-i)*min(heights[i],heights[j]),Max)
            if heights[i] < heights[j]:
                i += 1
            else:
                j -= 1
        return Max

        