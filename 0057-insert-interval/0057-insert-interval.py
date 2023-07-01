class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        ret = [] 
        #if len(intervals) == 0:
        #    return[newInterval]
          
        for i in range(len(intervals)):
            #if last<st or start>end: # not overlap 
            if intervals[i][0] > newInterval[1]:
                ret.append(newInterval)
                return ret + intervals[i:]
            elif intervals[i][1] < newInterval[0]:
                ret.append(intervals[i])
            else:
                newInterval = [min(intervals[i][0], newInterval[0]), max(intervals[i][1], newInterval[1])]
        ret.append(newInterval)
        return ret