from typing import List

# Time : Beats 88.49 %
# Memo : Beats 77.76 %
class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        x = max(nums)
        n=len(nums)
        max_count = 0
        ret=0
        L=0
        for R in range(n):
            if nums[R] == x:
                max_count += 1
            while max_count == k:
                if nums[L] == x:
                    max_count -=1
                L+=1
            ret += L
        
        return ret
    

# Time : Beats 98.29 %
# Memo : Beats 11.04 %
class Solution2:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        x=max(nums)
        maxi=[]
        ret=0
        maxc=0
        for R in range(len(nums)):
            if nums[R] == x:
                maxi.append(R)
                maxc+=1
            if maxc >= k:
                L = maxi[-k]
                ret += L+1
        return ret

# Time : Beats 99.69 %
# Memo : Beats 38.26 %
class Solution3:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        x = max(nums)
        last = len(nums)
        maxi=[]
        ret=0
        for i in range(last):
            if nums[i] == x:
                maxi.append(i)

        for R in range(len(maxi)-1,k-2,-1):
            freq = last-maxi[R]
            last = maxi[R]
            ret += (maxi[R-k+1]+1)*freq
        
        return ret

