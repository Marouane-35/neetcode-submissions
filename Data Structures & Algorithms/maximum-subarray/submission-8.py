class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        s=0
        max_s=nums[0]
        for el in nums  :
            if (el>=0 and s>=0) or (el<=0 and s>=0) :
                s+=el
                max_s=max(max_s,s)
                print(s)
            elif el>=0 :
                s=el
                print(s)
                max_s=max(max_s,s)
            elif el<=0 :
                s=el
                print(s)
                max_s=max(max_s,s)
            
            
        return max_s

        