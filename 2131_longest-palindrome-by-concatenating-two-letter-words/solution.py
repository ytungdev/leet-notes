from typing import List
from collections import Counter

# Time : Beats 96.75 %
# Memo : Beats 73.65 %
class Solution:
    def longestPalindrome(self, words: List[str]) -> int:
        counter = Counter(words)
        center = 0
        res = 0
        for word in counter.keys():
            drow = word[::-1]
            if word==drow:
                res += 4*(counter[word]//2)
                if center == 0 and counter[word]%2:
                    center = 1
            elif counter[word] > 0 and drow in counter:
                    res += min(counter[word], counter[drow]) * 4
                    counter[drow] = 0
        if center:
            res  += 2
        return res

# Time : Beats 44.41 %
# Memo : Beats 73.65 %
class Solution2:
    def longestPalindrome(self, words: List[str]) -> int:
        cnt = [[0]*26 for _ in range(26)]
        res = 0
        for word in words:
            c1 = ord(word[0]) - 97
            c2 = ord(word[1]) - 97
            # conterpart exist
            if cnt[c2][c1] > 0:
                res += 4
                cnt[c2][c1] -= 1
            # counterpart dont exist
            else:
                cnt[c1][c2] += 1
        # check for center
        for i in range(26):
            if cnt[i][i] == 1:
                res += 2
                break
        return res