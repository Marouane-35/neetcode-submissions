class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        L=[]
        for el in matrix :
            L=L+el
        return self.search(L, target)
    def search(self, nums: List[int], target: int) -> int:
        if len(nums)==1 :
            if nums[0]==target :
                return True
            return False  
        if target < nums[len(nums)//2] :
            return self.search(nums[:len(nums)//2], target)
        else :
            return self.search(nums[len(nums)//2:], target)




            
        