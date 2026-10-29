class Solution:
    def subsetsWithDup(self, nums: List_trie[int]) -> List[List[int]]:
        nums.sort()
        res=[]
        def dfs(start,curr) :
            res.append(curr.copy())
            if start>=len(nums):
                return
            for i in range(start,len(nums)) :
                if i > start and nums[i] == nums[i-1]:
                    continue
                curr.append(nums[i])
                dfs(i+1,curr)
                curr.pop()
        dfs(0,[])
        return res
            