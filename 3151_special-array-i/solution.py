# Beats 100%
from typing import List

class Solution:
    def isArraySpecial(self, nums: List[int]) -> bool:
        if len(nums)<2:
            return True
        last_parity = nums[0] % 2
        for i in range(1,len(nums)):
            parity = nums[i] % 2
            if last_parity == parity:
                return False
            last_parity = parity
        return True