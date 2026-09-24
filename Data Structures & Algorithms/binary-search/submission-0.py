class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if len(nums)==1 :
            if nums[0]==target :
                return 0
            return -1  
        if target < nums[len(nums)//2] :
            return self.search(nums[:len(nums)//2], target)
        else :
            if self.search(nums[len(nums)//2:], target) == -1 :
                return -1
            return self.search(nums[len(nums)//2:], target)+len(nums)//2

        