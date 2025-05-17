from typing import List

# Time : Beats 100.0 %
# Memo : Beats 83.24 %
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        L,M,R = 0,0,n-1

        while M<=R:
            if nums[M] == 0:
                nums[L],nums[M] = nums[M], nums[L]
                L += 1
                M += 1
            elif nums[M] == 1:
                M += 1
            else:
                nums[M], nums[R] = nums[R], nums[M]
                R -= 1

# Time : Beats 100.0 %
# Memo : Beats 11.82 %
class Solution1:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        for i in range(1,n):
            for j in range(i,0,-1):
                if nums[j] < nums[j-1]:
                    nums[j], nums[j-1] = nums[j-1],nums[j]
                else:
                    break

        