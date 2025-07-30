from typing import List

# Time : Beats 93.13 %
# Memo : Beats 44.64 %
class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        hi = 0
        max_len = 1
        cur_len = 1
        for num in nums:
            if num > hi:
                # start new streak
                hi = num
                cur_len = 1
                max_len = 1
            elif num == hi:
                # eexteend streak
                cur_len += 1
            else:
                # end and reset streak
                max_len = max(max_len, cur_len)
                cur_len = 0
        return max(max_len, cur_len)