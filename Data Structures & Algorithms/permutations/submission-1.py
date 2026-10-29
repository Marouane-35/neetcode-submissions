class Solution:
    def permute(self, nums: list[int]) -> list[list[int]]:
        res = []

        def dfs(i, curr):
            if i>= len(nums):
                res.append(curr.copy())
                return
            
            for j in range(len(nums)):
                if nums[j] in curr:
                    continue
                curr.append(nums[j])
                dfs(i+1, curr)
                curr.pop()
        dfs(0, [])
        return res