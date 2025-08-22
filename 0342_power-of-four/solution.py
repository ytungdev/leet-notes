# Time : Beats 100.0 %
# Memo : Beats 61.40 %
class Solution2:
    def isPowerOfFour(self, n: int) -> bool:
        return n & (n-1) == 0 and n & 1431655765 != 0

# Time : Beats 100.0 %
# Memo : Beats 61.40 %
class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        if n <= 0:
            return False
        while n > 1:
            if n % 4:
                return False
            n //= 4
        return True