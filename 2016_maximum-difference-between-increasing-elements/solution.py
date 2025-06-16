from typing import List

# Time : Beats 100.0 %
# Memo : Beats 89.57 %
class Solution:
    def maximumDifference(self, nums: List[int]) -> int:
        n = len(nums)
        
        min_i = 0
        max_diff = -1
        for i in range(1,n):
            if nums[i] > nums[min_i]:
                diff = nums[i] - nums[min_i]
                if diff > max_diff:
                    max_diff = diff
            else:
                min_i = i
        
        return max_diff