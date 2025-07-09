from typing import List

# Time : Beats 95.93 %
# Memo : Beats 58.52 %
class Solution:
    def maxFreeTime(self, eventTime: int, k: int, startTime: List[int], endTime: List[int]) -> int:
        '''
        total free time = sum of k+1 adjacent free time
        '''
        free = []
        d = 0
        total = 0
        # free time before first event
        # free time between eveents
        n = len(startTime)
        for i in range(n):
            l = startTime[i]-d
            free.append(l)
            total += l
            d = endTime[i]
        # free time after last event
        last = eventTime-d
        free.append(last)
        total += last

        # edge : no free time
        if total == 0:
            return 0
        
        # edge : able to rearrange all event 
        if k+1 >= len(free):
            return total

        # sliding window to find max
        curr = sum(free[:k+1])
        ret = curr
        for i in range(len(free)-k-1):
            curr = curr-free[i]+free[i+k+1]
            if curr > ret:
                ret = curr
        return ret