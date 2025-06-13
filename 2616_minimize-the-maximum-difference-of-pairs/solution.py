from typing import List

# Time : Beats 77.56 %
# Memo : Beats 40.16 %
class Solution:
    def minimizeMax(self, nums: List[int], p: int) -> int:
        if p == 0:
            return 0
        nums.sort()
        n = len(nums)
        
        def test(d):
            i,count =  0,0
            while i < n-1  and count<p:
                if nums[i+1]-nums[i] <= d:
                    i+=1
                    count+=1
                i+=1
            return count==p
                
        L,R = 0,nums[-1]-nums[0]
        while L<R:
            M=(L+R)//2
            if test(M):
                R=M
            else:
                L=M+1
        
        return L