from typing import List

# Time : Beats 100.00 %
# Memo : Beats  29.21 %

class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:
        for i in range(0,len(nums)-1):
            if nums[i] == nums[i+1]:
                nums[i] = nums[i] * 2
                nums[i+1] = 0
        res = [0]*len(nums)
        k = 0
        for j in range(len(nums)):
            if nums[j] != 0:
                res[k] = nums[j]
                k += 1
        return res
