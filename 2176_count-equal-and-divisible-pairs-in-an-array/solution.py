from typing import List

# Time : Beats 96.50 %
# Memo : Beats 48.17 %
class Solution:
    def countPairs(self, nums: List[int], k: int) -> int:
        _map = {}
        ret = 0
        for i in range(len(nums)):
            if nums[i] in _map:
                for j in _map[nums[i]]:
                    if (i*j)%k == 0:
                        ret += 1
                _map[nums[i]].append(i)
            else:
                _map[nums[i]] = [i]
        return ret