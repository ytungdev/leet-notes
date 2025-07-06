from typing import List
from collections import Counter

# Time : Beats 100.0 %
# Memo : Beats 21.90 %
class FindSumPairs:

    def __init__(self, nums1: List[int], nums2: List[int]):
        self.nums1 = nums1
        self.nums2 = nums2
        self.c1 = Counter(nums1)
        self.c2 = Counter(nums2)
        self.k1 = sorted(self.c1.keys())

    def add(self, index: int, val: int) -> None:
        self.c2[self.nums2[index]] -= 1
        if self.c2[self.nums2[index]] <= 0:
            del self.c2[self.nums2[index]]
        self.nums2[index] += val
        self.c2[self.nums2[index]] = self.c2.get(self.nums2[index],0) + 1
        # self.c2[self.nums2[index]] += 1
        # Counter('missing key') return 0 instead of KeyError, but have poorer performance

    def count(self, tot: int) -> int:
        ret = 0
        for n1 in self.k1:
            if n1 > tot:
                break
            counter = tot-n1
            if counter in self.c2:
                ret += self.c1[n1]*self.c2[counter]
        return ret



# Your FindSumPairs object will be instantiated and called as such:
# obj = FindSumPairs(nums1, nums2)
# obj.add(index,val)
# param_2 = obj.count(tot)