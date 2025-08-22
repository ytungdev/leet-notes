from typing import List

# Time : Beats 90.66 %
# Memo : Beats 96.14 %
class Solution:
    def zeroFilledSubarray(self, nums: List[int]) -> int:
        def count_ways(n):
            if n <= 1:
                return n
            return (1+n)*n//2
        ret = 0
        l = 0
        for num in nums:
            if num == 0:
                l += 1
            else:
                ret += count_ways(l)
                l = 0
        ret += count_ways(l)
        return ret