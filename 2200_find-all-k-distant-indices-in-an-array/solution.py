from typing import List

# Time : Beats 100.0 %
# Memo : Beats 90.91 %
class Solution:
    def findKDistantIndices(
        self, nums: List[int], key: int, k: int
    ) -> List[int]:
        res = []
        R = 0  # unjudged minimum index
        n = len(nums)
        for j in range(n):
            if nums[j] == key:
                L = max(R, j - k)
                R = min(n - 1, j + k) + 1
                for i in range(L, R):
                    res.append(i)
        return res
    

# Time : Beats 100.0 %
# Memo : Beats 68.60 %
class Solution:
    def findKDistantIndices(self, nums: List[int], key: int, k: int) -> List[int]:
        n = len(nums)
        
        if k>=n:
            return [i for i in range(n)]
        
        ret = set()
        for i in range(n):
            if key == nums[i]:
                L = max(0,i-k)
                R = min(n,i+k+1)
                for j in range(L,R):
                    ret.add(j)
        return list(ret)