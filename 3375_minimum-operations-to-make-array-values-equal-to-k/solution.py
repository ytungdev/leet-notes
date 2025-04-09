from typing import List

# Time : Beats 91.14 %
# Memo : Beats 52.91 %
# use set and iterate
class Solution2:
    def minOperations(self, nums: List[int], k: int) -> int:
        if min(nums) < k : 
            return -1
        
        res = set()
        for n in nums:
            if n > k and n not in res:
                res.add(n)

        return len(res)


# Time : Beats 86.48 %
# Memo : Beats  9.32 %
# sort and iterate
class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        nums.sort(reverse=True)

        if nums[-1] < k : 
            return -1
        if nums[0] == k:
            return 0
        
        last = nums[0]
        res = 0
        for num in nums:
            if num != last:
                res += 1
                last = num
            if num == k:
                return res
        if nums[-1] != k:
            res += 1
        return res