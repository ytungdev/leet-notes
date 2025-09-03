from typing import List

# Time : Beats 90.22 %
# Memo : Beats 32.11 %
class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        '''
        when second 0 appear, update max_len
        at most two segment, one before fisrt 0, one after
        '''
        n = len(nums)
        ret = 0
        curr = 0
        prev = 0
        for num in nums:
            if num:
                curr += 1
            else:
                ret = max(ret, curr+prev)
                prev = curr
                curr = 0
        if curr == n:
            return n-1
        else:
            return max(ret, curr+prev)
        
# Time : Beats 79.27 %
# Memo : Beats 97.89 %
class Solution2:
    def longestSubarray(self, nums: List[int]) -> int:
        n = len(nums)
        last_zero = -1
        L,R = 0,0
        ret = 0
        cur = 0
        while R<n:
            if nums[R] == 1:
                cur += 1
                R += 1
                continue
            # first zero, pass
            if last_zero == -1:
                last_zero = R
                R += 1
                continue
            ret = max(ret, cur)
            while L <= last_zero:
                cur -= 1
                L+=1
            L+=1
            last_zero = R
            R+=1
        if last_zero == -1:
            return n-1
        else:
            return max(ret, cur)