from typing import List

# Time : Beats 79.16 %
# Memo : Beats 82.46 %
class Solution:
    def maxSubsequence(self, nums: List[int], k: int) -> List[int]:
        sort_by_val = sorted(enumerate(nums), key=lambda x:x[1])
        sort_by_index = sorted(sort_by_val[-k:], key=lambda x:x[0])
        return [x[1] for x in sort_by_index]