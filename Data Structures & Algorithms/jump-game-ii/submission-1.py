class Solution:
    def jump(self, nums: List[int]) -> int:
        min_jumps = 0
        l = 0
        r = 0
        
        while r < len(nums) - 1:
            r_max = r
            for i in range(l, r + 1):
                r_max = max(r_max, i + nums[i])
            
            l = r + 1
            r = r_max
            min_jumps += 1
            
        return min_jumps