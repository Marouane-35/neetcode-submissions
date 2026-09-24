class Solution:
    def trap(self, height: List[int]) -> int:
        stack = []
        res = 0
        
        for i in range(len(height)):
            while stack and height[i] > height[stack[-1]]:
                fond = stack.pop()
                
                if not stack:
                    break
                    
                mur_gauche = stack[-1]
                
                largeur = i - mur_gauche - 1
                niveau_eau = min(height[i], height[mur_gauche])
                eau_ajoutee = niveau_eau - height[fond]
                
                res += largeur * eau_ajoutee
                
            stack.append(i)
            
        return res