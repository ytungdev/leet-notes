from typing import List

# Time : Beats 93.18 %
# Memo : Beats 34.47 %
class Solution:
    def partitionArray(self, nums: List[int], k: int) -> int:
        nums.sort()
        curr = nums[0]
        ret = 1
        for i in nums:
            if i > curr + k:
                curr = i
                ret += 1
        return ret
                
                