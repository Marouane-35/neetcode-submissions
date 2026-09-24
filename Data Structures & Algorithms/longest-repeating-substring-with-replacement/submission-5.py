class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        longuest=0
        freq=[0 for i in range(26)]
        L=0
        R=0
        while R<=len(s)-1 and L<=R:
            freq[ord(s[R].lower()) - 97]+=1
            if k>= (R-L+1)-max(freq) :
                longuest=max(longuest,R-L+1)
                R+=1
            else :
                L+=1
                longuest=max(longuest,R-L+1)
                freq[ord(s[L-1].lower()) - 97]-=1
                freq[ord(s[R].lower()) - 97]-=1
        return longuest








        