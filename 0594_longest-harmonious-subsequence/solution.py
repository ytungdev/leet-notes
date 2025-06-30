from typing import List
from collections import Counter

# Time : Beats 99.49 %
# Memo : Beats 21.92 %
class Solution:
    def findLHS(self, nums: List[int]) -> int:
        cnt = Counter(nums)
        ret = 0
        for num in cnt:
            if num+1 in cnt:
                ret = max(ret, cnt[num]+cnt[num+1])
        return ret