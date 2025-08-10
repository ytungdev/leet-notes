# Time : Beats 100.0 %
# Memo : Beats 82.67 %
class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        return n!=0 and n & (n-1) == 0

# Time : Beats 14.16 %
# Memo : Beats 12.32 %
class Solution2:
    def isPowerOfTwo(self, n: int) -> bool:
        m = 1
        while m<n:
            m *=2
        return m==n