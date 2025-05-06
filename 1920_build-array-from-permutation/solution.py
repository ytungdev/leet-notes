from typing import List

# Time : Beats 100.0 %
# Memo : Beats 34.10 %
class Solution:
    def buildArray(self, nums: List[int]) -> List[int]:
        res = []
        for num in nums:
            res.append(nums[num])
        return res