class Solution:
    def climbStairs(self, n: int) -> int:
        climb=[1,2]
        for i in range(2,n) :
            climb.append(climb[i-1]+climb[i-2])
        return climb[n-1]



        