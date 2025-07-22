from typing import List

# Time : Beats 98.72 %
# Memo : Beats 50.60 %
class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return nums[0]
        
        ret = 0
        curr_sum = 0
        L=0
        sub = set()
        for R in range(n):
            if nums[R] in sub:
                while nums[L] != nums[R]:
                    curr_sum -= nums[L]
                    sub.remove(nums[L])
                    L += 1
                L += 1
            else:
                curr_sum += nums[R]
                sub.add(nums[R])
                ret = max(ret, curr_sum)
        return ret
    
# Time : Beats 54.17 %
# Memo : Beats 78.00 %
class Solution2:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return nums[0]
        
        ret = nums[0]
        curr_sum = nums[0]
        L=0
        sub = {nums[0]:0}
        for R in range(1,n):
            if nums[R] in sub:
                while L <= sub[nums[R]]:
                    curr_sum -= nums[L]
                    L += 1
            curr_sum += nums[R]
            sub[nums[R]] = R
            ret = max(ret, curr_sum)
        return ret