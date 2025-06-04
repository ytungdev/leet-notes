from typing import List
from collections import deque

# Time : Beats 63.49 %
# Memo : Beats 27.12 %
class Solution:
    def maxCandies(self, status: List[int], candies: List[int], keys: List[List[int]], containedBoxes: List[List[int]], initialBoxes: List[int]) -> int:
        n = len(status)
        q = deque([])
        
        boxInv = set()
        waitlist = set() # have box but no key
        for b in initialBoxes:
            if status[b]:
                q.append(b)
                boxInv.add(b)
            else:
                waitlist.add(b)
        keyInv = set([i for i in range(n) if status[i]])
        
        res = 0
        while q:
            # only haveKey and haveBox will be added to q
            # each box is contained in one box at most
            i = q.popleft()
            res += candies[i]
            
            for key in keys[i]:
                if key not in keyInv:
                    keyInv.add(key)
                    if key in waitlist:
                        waitlist.remove(key)
                        q.append(key)
            
            for box in containedBoxes[i]:
                if box not in boxInv:
                    boxInv.add(box)
                    if box in keyInv:
                        q.append(box)
                    else:
                        waitlist.add(box)
        
        return res