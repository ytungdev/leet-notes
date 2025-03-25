# Beats 84.73%

from typing import List

class Solution:
    def countDays(self, days: int, meetings: List[List[int]]) -> int:
        meetings = sorted(meetings, key=lambda x:x[0])
        last_meeting = [0,0]
        ans = 0
        for meeting in meetings:
                a1,a2 = last_meeting
                b1,b2 = meeting
                # no overlap
                if b1 - a2 > 1:
                    ans+=b1-a2-1
                    last_meeting = meeting
                else:
                    last_meeting = min(a1,b1), max(a2,b2)
        ans += days - last_meeting[1]
        return ans
    

# Beats 93.64%

class Solution2:
    def countDays(self, days: int, meetings: List[List[int]]) -> int:
        meetings = sorted(meetings, key=lambda x:x[0])
        last_meeting = [0,0]
        ans = 0
        for meeting in meetings:
            if meeting[0] - last_meeting[1] > 1:
                ans+=meeting[0]-last_meeting[1]-1
                last_meeting = meeting
            else:
                last_meeting[1] = max(last_meeting[1],meeting[1])
        ans += days - last_meeting[1]
        return ans