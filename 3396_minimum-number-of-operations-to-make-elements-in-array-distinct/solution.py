from typing import List
import math


# Time : Beats 100.0 %
# Memo : Beats 27.88 %
# Use set() to store distinct number
class Solution2:
    def minimumOperations(self, nums: List[int]) -> int:
        distinct = set()
        for i in range(len(nums)-1, -1, -1):
            if nums[i] in distinct:
                return i//3 +1
            distinct.add(nums[i])
        return 0

# Time : Beats 78.88 %
# Memo : Beats 27.88 %
class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        for i in range(len(nums)-1, -1, -1):
            if nums[i] in nums[i+1:]:
                return math.ceil((i+1)/3)
        return 0