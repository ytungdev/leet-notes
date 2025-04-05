from typing import List

# Time : Beats 82.49 %
# Memo : Beats 95.94 %
class Solution1:
    def subsetXORSum(self, nums: List[int]) -> int:
        def dfs(i, res):
            if i == len(nums):
                return res
            return dfs(i+1,res^nums[i]) + dfs(i+1,res)
        return dfs(0,0)


# Time : Beats 18.20 %
# Memo : Beats  5.22 %
class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        subsets = []
        def dfs(avail_nums, curr_path):
            subsets.append(curr_path)
            for i in range(len(avail_nums)):
                dfs(avail_nums[i+1:],curr_path+[avail_nums[i]])
        dfs(nums,[])

        res = 0
        for subset in subsets:
            sum = 0
            for n in subset:
                sum ^= n
            res += sum

        return res