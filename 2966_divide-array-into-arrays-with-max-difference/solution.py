from typing import List

# Time : Beats 96.61 %
# Memo : Beats 74.46 %
class Solution:
    def divideArray(self, nums: List[int], k: int) -> List[List[int]]:
        n=len(nums)
        res = [0]*(n//3)
        nums.sort()
        for i in range(0,n,3):
            if nums[i]+k < nums[i+2]:
                return []

            res[i//3] = [nums[i],nums[i+1],nums[i+2]]
        
        return res