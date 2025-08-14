# Time : Beats 80.05 %
# Memo : Beats 72.69 %
class Solution2:
    def isPowerOfThree(self, n: int) -> bool:
        return n > 0 and 1162261467 % n == 0

# Time : Beats 47.84 %
# Memo : Beats 43.93 %
class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        if n <= 0:
            return False
        while n > 1:
            if n % 3:
                return False
            n //= 3
        return True