class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        L1=list(s1)
        L=0
        R=0
        while L1 and R<len(s2):
            if s2[R] in L1 :
                L1.remove(s2[R])
                R+=1
                
            else :
                if s2[L] in s1 :
                    L1.append(s2[L]) 
                L+=1
                R=max(L,R)
        return len(L1)==0 
        