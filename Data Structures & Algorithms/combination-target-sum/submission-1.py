class Solution:
    def combinationSum(self, nums: List[int], target: int, start_index : int=0, path: List[int]=None, output: List[List[int]]=None) -> List[List[int]]:
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
            path.append(nums[i])
            self.combinationSum(nums, target-nums[i],i,path,output)
            path.pop()  #Backtracking

        return output