from typing import List

# Time : Beats 96.90 %
# Memo : Beats 54.26 %
class Solution:
    def maximumLength(self, nums: List[int]) -> int:
        '''
        - 00000
        - 11111
        - 01010
        - 10101
        '''
        c00 = 0
        c01 = 0

        c01_odd = nums[0] % 2

        for n in nums:
            if n%2 == 0:
                c00 += 1
                if c01_odd == 0:
                    c01 += 1
                    c01_odd ^= 1
            elif c01_odd == 1:
                c01 += 1
                c01_odd ^= 1
    
        return max(c00,len(nums)-c00,c01)