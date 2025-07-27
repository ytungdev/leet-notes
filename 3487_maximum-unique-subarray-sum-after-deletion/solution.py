from typing import List

# Time : Beats 100.0 %
# Memo : Beats 14.13 %
class Solution:
    def maxSum(self, nums: List[int]) -> int:
        ret = 0
        seen = set()
        maxv = float('-inf')
        for num in nums:
            if num <= 0:
                maxv = max(maxv, num)
            else:
                if num not in seen:
                    ret += num
                    seen.add(num)
        return ret if ret > 0 else maxv