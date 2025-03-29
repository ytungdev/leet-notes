# Beats 35.84%

from typing import List

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        i,j = 0,0
        m,n = len(nums1), len(nums2)
        nums = []
        while i< m and j < n:
            if nums1[i] <= nums2[j]:
                nums.append(nums1[i])
                i+=1
            else:
                nums.append(nums2[j])
                j+=1
        nums += nums1[i:]
        nums += nums2[j:]
        if (m+n)%2 :
            return nums[(m+n)//2]
        else:
            return (nums[(m+n)//2] + nums[(m+n)//2-1])/2