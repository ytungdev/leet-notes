class Solution:
    def minOperations(self, nums: List[int]) -> int:
        count = 0
        for i in range(len(nums)-2):
            if nums[i] == 1:
                continue
            else:
                nums[i:i+3] = [1-x for x in nums[i:i+3]]
                count += 1
        return count if all(nums) else -1
