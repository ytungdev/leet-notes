from typing import List

# Time : Beats 66.49 %
# Memo : Beats 70.31 %

class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if sum(nums)%2:
            return False

        target = sum(nums)//2
        
        dp = [True]+[False]*target
        for num in nums:
            for currSum in range(target, num-1, -1):
                dp[currSum] = dp[currSum] or dp[currSum-num]
        
        return dp[target]