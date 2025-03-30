from typing import List

# Time : Beats 100.0 %
# Memo : Beats 62.61 %

class Solution:
    def mergeArrays(self, nums1: List[List[int]], nums2: List[List[int]]) -> List[List[int]]:
        res = []
        i,j = 0,0
        m,n = len(nums1),len(nums2)
        while i<m and j<n:
            if nums1[i][0] == nums2[j][0]:
                res.append([nums1[i][0], nums1[i][1] + nums2[j][1]])
                i+=1
                j+=1
            elif nums1[i][0] < nums2[j][0]:
                res.append(nums1[i])
                i+=1
            else:
                res.append(nums2[j])
                j+=1
        if i<m:
            res.extend(nums1[i:])
        if j<n:
            res.extend(nums2[j:])
        return res
