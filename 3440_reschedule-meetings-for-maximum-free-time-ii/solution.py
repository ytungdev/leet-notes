from typing import List

# Time : Beats 35.47 %
# Memo : Beats  6.16 %
class Solution:
    def maxFreeTime(self, eventTime: int, startTime: List[int], endTime: List[int]) -> int:
        '''
        - for n event, there are n+1 gap
        - two way to reschedule
            1. swap to non-adjacent gap, if gap>=dur
            2. swap to adjacent gap
        - method 2 can yield longer gap
        '''
 
        n = len(startTime)

        # construct gap
        last = 0
        gap_sorted = [] # (idx,length)
        gap_unsort = []
        for i in range(n):
            l = startTime[i] - last
            gap_sorted.append((i,l))
            gap_unsort.append(l)
            last = endTime[i]
        l = eventTime - last
        gap_sorted.append((n,l))
        gap_unsort.append(l)
        
        gap_sorted.sort(reverse=True,key=lambda x:x[1])
        # enumerate
        ret = 0
        for i in range(n):
            l = endTime[i] - startTime[i]
            total = gap_unsort[i] + gap_unsort[i+1] + l
            if total < ret:
                continue

            # test for swapping with adj gap
            ret = max(ret,gap_unsort[i] + gap_unsort[i+1])

            # test for swapping with non-adj gap
            for j in range(n+1):
                if gap_sorted[j][1] < l:
                    break
                if gap_sorted[j][0] in [i,i+1]:
                    continue
                ret = total
        return ret
        '''
        for events[0], gap[0] and gap[1] is adjacent
        for events[1], gap[1] and gap[2] is adjacent
        '''