class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort()
        ans=0
        prev = intervals[0][1]
        for i in range(1, len(intervals)):
            if prev > intervals[i][0]:
                ans+=1
                prev = min(prev,intervals[i][1])
            else:
                prev = intervals[i][1]

        return ans