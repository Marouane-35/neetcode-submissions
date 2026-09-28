class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        output=[[]]
        for num in nums :
            new_subsets=[[num]+out for out in output ]
            output.extend(new_subsets)
        return output
