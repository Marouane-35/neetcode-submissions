class Solution:
    def canJump(self, nums: List[int]) -> bool:
        max_reach=0
        for i,num in enumerate(nums) :
            if max_reach>=i :
                max_reach=max(max_reach,i+nums[i])
        return max_reach+1>=len(nums)
      