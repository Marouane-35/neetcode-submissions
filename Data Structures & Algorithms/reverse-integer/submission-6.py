class Solution:
    def reverse(self, x: int) -> int:
            m=abs(x)
            L=[]
            while m != 0:
                L.append(m%10)
                m=m//10
            ch = "".join(str(x) for x in L)
            try:
                ch=int(ch)
            except ValueError:
                return 0
            if x<0 :
                ch= -ch
            if not -2**31<=ch<=2**31-1 :
                return 0
            return ch