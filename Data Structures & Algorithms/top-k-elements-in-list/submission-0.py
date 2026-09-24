class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        compteur = {}
        for num in nums:
            compteur[num] = compteur.get(num, 0) + 1
            
        seaux = [[] for i in range(len(nums) + 1)]
        
        for num, frequence in compteur.items():
            seaux[frequence].append(num)
            
        resultat = []
        for i in range(len(seaux) - 1, 0, -1):
            for num in seaux[i]:
                resultat.append(num)
                if len(resultat) == k:
                    return resultat