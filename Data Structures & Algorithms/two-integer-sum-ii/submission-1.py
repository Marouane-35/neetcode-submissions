class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        r=len(numbers)-1
        l=0
        while numbers[r]+numbers[l]!=target and r>l:
            if numbers[r]+numbers[l] < target :
                l+=1
            else :
                r-=1
        return [l+1,r+1]
