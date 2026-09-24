class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        def Fusion(L1,L2) :
            L=[]
            i1=0
            i2=0
            while i1<len(L1) and i2<len(L2) :
                if L1[i1][0]<L2[i2][0] :
                    L.append(L1[i1])
                    i1+=1
                else :
                    L.append(L2[i2])
                    i2+=1
            return L + L1[i1:] + L2[i2:]

        def tri(intervals) :
            if len(intervals)<=1 :
                return intervals
            m=len(intervals)//2
            return Fusion(tri(intervals[:m]),tri(intervals[m:]))
        intervals=tri(intervals)
        L=[]
        L.append(intervals[0])
        for interval in intervals[1:] :
            if not L[-1][1]<interval[0] :
                L[-1][0]=L[-1][0]
                L[-1][1]=max(L[-1][1],interval[1])
            else :
                L.append(interval)
        return L


        
        