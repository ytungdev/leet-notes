from typing import List

# Time : Beats 100.0 %
# Memo : Beats 82.11 %
# 1-pass
class Solution2:
    def maximumTripletValue(self, nums: List[int]) -> int:
        size = len(nums)

        if size == 3:
            return max((nums[0] - nums[1]) * nums[2],0)
        
        max_i = nums[0]
        max_diff = 0
        res = 0

        for k in range(2,size):
            max_i = max(max_i, nums[k-2])
            max_diff = max(max_diff, max_i - nums[k-1])
            res = max(res, max_diff*nums[k])

        return res



# Time : Beats 34.56 %
# Memo : Beats 82.11 %
# Naive - 3 nested loop
class Solution:
    def maximumTripletValue(self, nums: List[int]) -> int:
        size = len(nums)

        if size == 3:
            return max((nums[0] - nums[1]) * nums[2],0)

        res = 0
        for i in range(size-2):
            for j in range(i+1, size-1):
                for k in range(j+1, size):
                    ans = (nums[i] - nums[j]) * nums[k]
                    res = max(ans,res)
        return res

