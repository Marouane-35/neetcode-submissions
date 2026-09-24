class Solution:
    def reverse(self, x: int) -> int:
        result = 0
        m = abs(x)
        
        while m != 0:
            result = (result * 10) + (m % 10)
            m = m // 10
            
        if x < 0:
            result = -result
            
        if result < -2**31 or result > 2**31 - 1:
            return 0
            
        return result