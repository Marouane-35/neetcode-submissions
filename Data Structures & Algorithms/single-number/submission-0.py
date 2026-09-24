class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        seen={}
        potential=[]
        for el in nums :
            if el in seen :
                potential.remove(el)
            else :
                seen[el]=1
                potential.append(el)
        return potential[0]

        