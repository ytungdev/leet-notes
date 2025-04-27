from typing import List

# Time : Beats 93.99 %
# Memo : Beats 16.83 %
class Solution:
    def countSubarrays(self, nums: List[int], minK: int, maxK: int) -> int:
        count = 0
        start = 0
        minI, maxI = -1,-1
        for i in range(len(nums)):
            if nums[i] < minK or nums[i] > maxK:
                start = i + 1
                minI, maxI = -1,-1
                continue
            if nums[i] == minK:
                minI = i
            if nums[i] == maxK:
                maxI = i
            if minI != -1 and maxI != -1:
                count += min(maxI, minI) - start + 1
           
        return count