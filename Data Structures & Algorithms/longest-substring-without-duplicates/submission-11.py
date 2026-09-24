class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0:
            return 0
        else :
            seen={}
            left=0
            longuest=1
            for i in range(len(s)) :
                if s[i] in seen and seen[s[i]]>=left :
                    longuest=max(longuest,i-1-left)
                    left=seen[s[i]]+1
                seen[s[i]]=i
                longuest = max(longuest, i - left + 1)
        return longuest
