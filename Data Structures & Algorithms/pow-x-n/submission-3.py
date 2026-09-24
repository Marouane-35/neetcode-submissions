class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n<0 :
            return 1/self.myPow(x,-n)
        if n==0 :
            return 1
        middle=self.myPow(x,n//2)
        if n%2==0:
            return middle*middle
        else :
            return x*middle*middle
        