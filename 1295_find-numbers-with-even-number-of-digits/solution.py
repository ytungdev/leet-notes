from typing import List

# Time : Beats 100.0 %
# Memo : Beats 83.23 %
class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        ret = 0
        for num in nums:
            if len(str(num)) % 2 == 0:
                ret+=1
        return ret