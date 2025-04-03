from typing import List

# Time : Beats 78.23 %
# Memo : Beats 97.72 %

class Solution:
    def maximumTripletValue(self, nums: List[int]) -> int:
        max_i = max_diff = res = 0

        for k in nums:
            res = max(res, max_diff*k)
            max_i = max(max_i, k)
            max_diff = max(max_diff, max_i - k)

        return res