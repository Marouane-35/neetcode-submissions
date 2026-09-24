class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        D=defaultdict(list)
        for mot in strs :
            clé = [0 for i in range(26)]
            for lettre in mot :
                clé[ord(lettre)-ord('a')]+=1
            D[tuple(clé)].append(mot)
        return list(D.values())