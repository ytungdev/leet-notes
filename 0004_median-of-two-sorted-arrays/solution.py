from typing import List


# Time : Beats 100.0 %
# Memo : Beats 84.02 %
class Solution2:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        m,n = len(nums1), len(nums2)
    
        # make sure nums1 is smaller in size
        if m>n:
            nums1,nums2 = nums2,nums1
            m,n = n,m

        total = m+n
        half = total//2

        L,R = 0, m-1            # search range in nums1
        while True:
            i = (L+R)//2        # partition in nums1
            j = half - i - 2    # partition in nums2
            L1 = nums1[i] if i >= 0 else float("-inf")
            R1 = nums1[i+1] if (i+1) < m else float("inf")
            L2 = nums2[j] if j >= 0 else float("-inf")
            R2 = nums2[j+1] if (j+1) < n else float("inf")
            if L1 <= R2 and L2 <= R1:
                a = max(L1,L2)
                b = min(R1,R2)
                if (m+n)%2:
                    return b
                else:
                    return (a+b)/2
            if L1 > R2:         # search nums1.left
                R = i-1
            else:               # search nums1.right
                L = i+1

# Time : Beats 35.84 %
# Memo : Beats 59.92 %
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