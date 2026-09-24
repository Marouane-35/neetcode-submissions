class Solution:
    def isHappy(self, n: int) -> bool:
        def squares_sum(n) :
            s=0
            while n!=0 :
                s+=(n%10)**2
                n=n//10
            return s
        seen=set()
        a=0
        while n not in seen and a!=1:
            seen.add(n)
            a=squares_sum(n)
            n=a
        if a==1:
            return True
        return False

        