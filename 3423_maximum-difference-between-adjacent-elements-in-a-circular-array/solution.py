from typing import List

# Time : Beats 100.0 %
# Memo : Beats 96.14 %
class Solution:
    def maxAdjacentDistance(self, nums: List[int]) -> int:
        nums.append(nums[0])
        ret = 0
        for i in range(1,len(nums)):
            diff = abs(nums[i]-nums[i-1])
            if diff > ret:
                ret = diff
        return ret