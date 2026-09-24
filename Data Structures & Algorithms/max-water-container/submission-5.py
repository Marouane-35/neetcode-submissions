class Solution:
    def maxArea(self, heights: List[int]) -> int:
        S=0
        l=0
        r=len(heights)-l-1
        S=max(S,min(heights[l],heights[r])*(r-l))
        while l<r:
            if heights[l] > heights[r] :
                r-=1
            else :
                l+=1
            S=max(S,min(heights[l],heights[r])*(r-l))
        return S