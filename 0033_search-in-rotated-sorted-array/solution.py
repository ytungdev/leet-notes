from typing import List

# Time : Beats  0.15 %
# Memo : Beats 98.93 %

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        def bin_search(nums, start, end, target):
            mid = (end-start)//2 + start
            if nums[mid] == target:
                return mid
            if start >= end:
                return -1
            if nums[mid] > target:
                return bin_search(nums, start, mid, target)
            else:
                return bin_search(nums, mid+1, end, target)

        def pivot_search(nums, start, end):
            mid = (end-start)//2 + start
            if start == end:
                return start
            if nums[mid] > nums[end]:
                return pivot_search(nums, mid+1, end)
            else:
                return pivot_search(nums, start, mid)

        if not nums:
            return -1
    
        start, end = 0, len(nums)-1
        pivot = pivot_search(nums, start, end)
        if nums[pivot] == target:
            return pivot
        if nums[end] >= target:
            return bin_search(nums, pivot, end, target)
        else:
            return bin_search(nums, start, pivot-1, target)