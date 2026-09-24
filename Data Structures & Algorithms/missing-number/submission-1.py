class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        suspects={i for i in range(len(nums)+1)}
        for i in range(len(nums)) :
            suspects.remove(nums[i])
        return suspects.pop()    