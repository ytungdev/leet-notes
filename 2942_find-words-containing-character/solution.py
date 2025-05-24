from typing import List

# Time : Beats 100.0 %
# Memo : Beats 68.13 %
class Solution:
    def findWordsContaining(self, words: List[str], x: str) -> List[int]:
        res = []
        for i in range(len(words)):
            if x in words[i]:
                res.append(i)
        return res