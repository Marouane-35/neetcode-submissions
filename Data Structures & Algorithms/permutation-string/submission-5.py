class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        count1 = {}

        for s in s1:
            count1[s] = count1.get(s, 0) + 1
        
        count2 = {}

        if len(s2) < len(s1):
            return False
        
        for i in range(len(s2)):
            if i < len(s1):
                count2[s2[i]] = count2.get(s2[i], 0) + 1
            else:
                flag = True
                for key in count1:
                    if key not in count2 or count2[key] != count1[key]:
                        flag = False
                if flag:
                    return flag

                count2[s2[i]] = count2.get(s2[i], 0) + 1
                old_idx = i - len(s1)
                count2[s2[old_idx]] -= 1

        flag = True
        for key in count1:
            if key not in count2 or count2[key] != count1[key]:
                flag = False            
        if flag:                    
            return flag

        return False
    