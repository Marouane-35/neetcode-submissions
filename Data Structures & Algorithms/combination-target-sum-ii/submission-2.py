class Solution:
    def combinationSum2(self, nums: List[int], target: int, start_index : int=0, path: List[int]=None, output: List[List[int]]=None) -> List[List[int]]:
        nums.sort()
        if path is None :
            path=[]
        if output is None :
            output=[]
        
        if target == 0 :
            output.append(path.copy())
            return output

        if target <0 :
            return output

        for i in range(start_index,len(nums)) :
            if i > start_index and nums[i] == nums[i - 1]:
                continue   
            path.append(nums[i])
            self.combinationSum2(nums, target-nums[i],i+1,path,output)
            path.pop()  #Backtracking

        return output