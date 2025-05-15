from typing import List

# Time : Beats 100.0 %
# Memo : Beats 22.03 %
class Solution:
    def getLongestSubsequence(self, words: List[str], groups: List[int]) -> List[str]:
        res = []
        grp = groups[0]
        for i in range(len(groups)):
            if groups[i] == grp:
                res.append(words[i])
                grp ^= 1
        return res