from typing import List

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        if len(nums) <= 1:
            return [nums]
        
        output = []
        for i in range(len(nums)):
            num = nums[i]
            remaining = nums[:i] + nums[i+1:]
            for p in self.permute(remaining):
                output.append([num] + p)
                
        return output