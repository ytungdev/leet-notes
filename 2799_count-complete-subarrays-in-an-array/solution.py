from typing import List

# Time : Beats 78.46 %
# Memo : Beats  5.64 %
class Solution:
    def countCompleteSubarrays(self, nums: List[int]) -> int:
        u = len(set(nums))
        n = len(nums)

        if u == 1:
            return (1+n)*n//2

        cnt = 0
        R=0
        freq = {}
        for L in range(n):
            if L > 0:
                remove = nums[L-1]
                freq[remove] -= 1
                if freq[remove] == 0:
                    freq.pop(remove)
            while R<n and len(freq) < u:
                add = nums[R]
                freq[add] = freq.get(add,0) + 1
                R += 1
            if len(freq) == u:
                cnt += n - R +1
        return cnt