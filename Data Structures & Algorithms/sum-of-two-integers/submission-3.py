class Solution:
    def getSum(self, a: int, b: int) -> int:
        a &= 0xFFFFFFFF
        b &= 0xFFFFFFFF
        result=0
        reste=0
        for i in range(32):
            bit_a=(a >> i)&1
            bit_b=(b >> i)&1
            ajout=bit_a^bit_b^reste
            reste = (bit_a & bit_b) | (reste & (bit_a ^ bit_b))            
            result |= ajout << i
        return result if result <= 0x7FFFFFFF else ~(result ^ 0xFFFFFFFF)




        