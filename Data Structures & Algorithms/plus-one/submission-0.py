class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        r=sum(digits[i]*10**(len(digits)-1-i) for i in range(len(digits)))+1
        return list(str(r))
        