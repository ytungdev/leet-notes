from typing import List

# Time : Beats 100.0 %
# Memo : Beats 98.38 %

class Solution:
    def numRabbits(self, answers: List[int]) -> int:
        grp = {}
        ret = 0
        for i in answers:
            if i == 0:
                # unique
                ret += 1
                continue
            if i not in grp:
                # first of grp[i]
                grp[i] = i
                ret += i+1
            else:
                grp[i] -= 1
                if grp[i] == 0:
                    # grp[i] fulled
                    del grp[i]

        return ret
        