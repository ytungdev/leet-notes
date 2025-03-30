from typing import List

# Time : Beats 55.36 %
# Memo : Beats 84.42 %
class Solution1:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)
        ans = []
        for i in range(len(nums)-2):
            # Skip duplicates
            if i > 0 and nums[i - 1] == nums[i]:
                continue 
            compliment = 0 - nums[i]
            L,R = i+1,len(nums)-1
            while L<R:
                total = nums[L]+nums[R]
                if total == compliment:
                    ans.append((nums[i], nums[L], nums[R]))
                    R -= 1
                    L += 1
                    # Skip duplicates
                    while L<R and nums[L-1] == nums[L]:
                        L += 1
                    # Skip duplicates
                    while L<R and nums[R+1] == nums[R]:
                        R -= 1
                elif total > compliment:
                    R -= 1
                else:
                    L += 1
        return ans


# Time : Beats 12.91 %
# Memo : Beats 17.36 %
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)
        ans = set()
        for i in range(len(nums)-2):
            compliment = 0 - nums[i]
            L,R = i+1,len(nums)-1
            while L<R:
                total = nums[L]+nums[R]
                if total == compliment:
                    ans.add((nums[i], nums[L], nums[R]))
                if total > compliment:
                    R -= 1
                else:
                    L += 1
        return ans
