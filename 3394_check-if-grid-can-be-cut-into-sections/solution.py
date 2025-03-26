# Beats 69.44%

from typing import List

class Solution:
    def checkValidCuts(self, n: int, rectangles: List[List[int]]) -> bool:
        def merge(intervals):
            result = []
            last_interval = intervals[0]
            for interval in intervals[1:]:
                if interval[0] >= last_interval[1]:
                    # no overlap -> add interval
                    result.append(last_interval)
                    last_interval = interval
                else:
                    # overlap -> extend interval
                    last_interval[1] = max(interval[1], last_interval[1])
            result.append(last_interval)
            return result

        x_range = []
        y_range = []
        for rect in rectangles:
            x1,y1,x2,y2 = rect
            x_range.append([x1,x2])
            y_range.append([y1,y2])
        x_range = sorted(x_range, key=lambda x:x[0])
        y_range = sorted(y_range, key=lambda x:x[0])
        
        x_interval = merge(x_range)
        y_interval = merge(y_range)
        return len(y_interval) >= 3 or len(x_interval) >= 3