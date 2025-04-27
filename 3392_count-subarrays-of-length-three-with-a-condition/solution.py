from typing import List

# Time : Beats 91.43 %
# Memo : Beats 45.92 %
class Solution:
    def countSubarrays(self, nums: List[int]) -> int:
        i = 1
        ret = 0
        while i < len(nums)-1:
            if (nums[i-1]+nums[i+1])*2 == nums[i]:
                ret+=1
            i+=1
        return ret