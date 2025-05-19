from typing import List

# Time : Beats 100.0 %
# Memo : Beats 80.13 %
# set()
class Solution:
    def triangleType(self, nums: List[int]) -> str:
        # a+b <= c 
        # a+c <= b
        # b+c <= a
        if nums[0] + nums[1] <= nums[2]:
            return "none"
        if nums[0] + nums[2] <= nums[1]:
            return "none"
        if nums[1] + nums[2] <= nums[0]:
            return "none"
        s = len(set(nums))
        if s == 1: return "equilateral"
        if s == 2: return "isosceles"
        return "scalene"

# Time : Beats 100.0 %
# Memo : Beats 51.59 %
# sort
class Solution1:
    def triangleType(self, nums: List[int]) -> str:
        # let a<=b<=c
        if nums[0] > nums[1]:
            nums[0], nums[1] = nums[1], nums[0]
        if nums[1] > nums[2]:
            nums[1], nums[2] = nums[2], nums[1]
        if nums[0] > nums[1]:
            nums[0], nums[1] = nums[1], nums[0]
        
        if nums[0]+nums[1]<=nums[2]:
            return "none"
        if nums[0] ==  nums[2]:
            return "equilateral"
        # acute/obtuse
        if nums[1] == nums[2] or nums[0] == nums[1]:
            return "isosceles"
        return "scalene"