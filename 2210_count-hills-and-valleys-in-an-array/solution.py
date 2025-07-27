from typing import List

# Time : Beats 100.0 %
# Memo : Beats 39.14 %
## 1-pass
class Solution:
    def countHillValley(self, nums: List[int]) -> int:
        ret = 0
        prev = nums[0]
        for i in range(1,len(nums)-1):
           if nums[i] != nums[i+1]:
                if prev < nums[i] > nums[i+1] or prev > nums[i] < nums[i+1]:
                    ret += 1
                prev = nums[i]
        return ret 

        
# Time : Beats 100.0 %
# Memo : Beats 64.44 %
## 2-pass
class Solution2:
    def countHillValley(self, nums: List[int]) -> int:
        num_set = [nums[0]]
        for num in nums:
            if num != num_set[-1]:
                num_set.append(num)
        n = len(num_set)

        if n < 3:
            return 0

        down = -1 if num_set[0] > num_set[1] else 1

        ret = 0
        for i in range(2,n):
            if num_set[i]*down < num_set[i-1]*down:
                ret += 1
                down *= -1
        return ret

        



            


            
