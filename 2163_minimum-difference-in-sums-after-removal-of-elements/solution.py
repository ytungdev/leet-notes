from typing import List
from collections import heapq

# Time : Beats 39.06 %
# Memo : Beats  5.28 %
class Solution:
    def minimumDifference(self, nums: List[int]) -> int:
        '''
        Objective:
            - min : sum_L - sum_R
            - min:sum_L and max:sum_R
        0 1 2 3 4 5
        a b c d e f
        - dp_l[i] = sum of min n element in [nums[0]..nums[i]]
            - max heap of size n
            - preprocess first n element (dp[n-1])
        - dp_r[i] = sum of max n element in [nums[i+1]..nums[-1]]
            - min heap of size n
            - preprocess last n element (dp[l-n-1])
        '''

        l = len(nums)
        n = l//3

        # create max heap to find min sum for dp table
        dp_l = [0]*l
        heap_l = [-x for x in nums[:n]]
        heapq.heapify(heap_l)
        curr = sum(heap_l)
        dp_l[n-1] = curr
        for i in range(n,l):
            rmv = heapq.heappushpop(heap_l,-nums[i])
            curr = curr - rmv - nums[i] # negate
            dp_l[i] = curr
        
        # create min heap to find max sum for dp table
        dp_r = [0]*l
        heap_r = nums[l-n:]
        heapq.heapify(heap_r)
        curr = sum(heap_r)
        dp_r[l-n-1] = curr
        for i in range(l-n-2,-1,-1):
            rmv = heapq.heappushpop(heap_r,nums[i+1])
            curr = curr - rmv + nums[i+1]
            dp_r[i] = curr
        
        ret = float('inf')
        for i in range(n-1,l-n):
            ret = min(ret, -dp_l[i]-dp_r[i])
        return ret