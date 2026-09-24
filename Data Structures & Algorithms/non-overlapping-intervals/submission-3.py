class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        if len(intervals)<=1 :
            return 0
        intervals.sort(key=lambda x: x[1])
        c=0
        end=intervals[0][1]
        for interval in intervals[1:] :
            if interval[0]< end :
                c+=1
            else :
                end=interval[1]
        return c
            
        