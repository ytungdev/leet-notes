from typing import List

# Beats 71.30%
class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        a,b,c = [],[],[]
        for i in nums:
            if i == pivot:
                b.append(i)
            elif i < pivot:
                a.append(i)
            else:
                c.append(i)
        return a+b+c
    
# Beats 91.22%
class Solution2:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        hi,lo = [],[]
        p = [pivot]*nums.count(pivot)
        for i in nums:
            if i > pivot:
                hi.append(i)
            elif i < pivot:
                lo.append(i)
        return lo+p+hi