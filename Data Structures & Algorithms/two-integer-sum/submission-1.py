class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        deja_vu={}
        for i in range(len(nums)) :
            complement = target - nums[i]
            if complement in deja_vu.keys() :
                return [deja_vu[complement],i]
            deja_vu[nums[i]]=i
        return []


        