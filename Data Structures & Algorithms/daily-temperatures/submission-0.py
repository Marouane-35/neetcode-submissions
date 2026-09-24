class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        output=[0 for i in range(len(temperatures))]
        left=[0]
        for i in range(len(temperatures)) :
            while left and temperatures[i]>temperatures[left[-1]] :
                output[left[-1]]=i-left[-1]
                left.pop()
            left.append(i)
        return output