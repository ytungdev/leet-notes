from typing import List

# Time : Beats 100.0 %
# Memo : Beats 36.37 %
class Solution:
    def isZeroArray(self, nums: List[int], queries: List[List[int]]) -> bool:
        n = len(nums)
        d = [0]*(n+1)
        for L,R in queries:
            d[L] += 1
            d[R+1] -= 1
        # a[i] = d[i] + a[i-1]
        steps = 0
        for i in range(n):
            steps += d[i]
            if nums[i] - steps > 0:
                return False
        return True