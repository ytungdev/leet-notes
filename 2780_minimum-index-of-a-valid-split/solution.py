
from typing import List
from collections import Counter

# Beats 89.39% : use collectins.Counter
class Solution3:
    def minimumIndex(self, nums: List[int]) -> int:
        freq = Counter(nums)
        dominant, freq_d = max(freq.items(), key=lambda x : x[1])

        freq_L = 0
        freq_R = freq_d

        for i in range(len(nums)-1):
            if nums[i] == dominant:
                freq_L += 1
                freq_R -= 1

                if freq_L * 2 > i + 1 and freq_R * 2 > len(nums) - i -1:
                    return i
        return -1

# Beats 43.37% : only keep track of freq of dom in both subarray
class Solution2:
    def minimumIndex(self, nums: List[int]) -> int:
        freq_L = {i:0 for i in nums}
        freq_R = {i:0 for i in nums}

        for i in nums:
            freq_R[i] += 1
        dominant = max(freq_R, key=lambda x: freq_R[x])

        for i in range(len(nums)-1):
            n = nums[i]
            freq_L[n] += 1
            freq_R[n] -= 1
            
            if freq_L[dominant] * 2 <= i + 1:
                continue
            else:
                if freq_R[dominant] * 2 > len(nums) - i -1:
                    return i
        return -1


# Beats 9.58%
class Solution:
    def minimumIndex(self, nums: List[int]) -> int:
        freq_L = {i:0 for i in nums}
        freq_R = {i:0 for i in nums}

        for i in nums:
            freq_R[i] += 1
        dominant = max(freq_R, key=lambda x: freq_R[x])

        for i in range(len(nums)-1):
            n = nums[i]
            freq_L[n] += 1
            freq_R[n] -= 1
            
            if freq_L[dominant] * 2 <= i + 1:
                continue
            else:
                if freq_R[dominant] * 2 > len(nums) - i -1:
                    return i
        return -1