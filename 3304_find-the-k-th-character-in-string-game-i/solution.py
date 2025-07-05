from typing import List

# Time : Beats 100.0 %
# Memo : Beats 17.72 %
class Solution:
    def kthCharacter(self, k: int) -> str:
        step = 0
        while k > 1:
            order = k.bit_length() - 1
            # if k==2**i
            if (1<<order) == k:
                return chr(97+step+order)
            k -= 1<<order
            step += 1
        return chr(97+step)