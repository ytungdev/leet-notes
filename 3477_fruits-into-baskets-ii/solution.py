from typing import List

# Time : Beats 88.24 %
# Memo : Beats 17.58 %
# deleting
class Solution:
    def numOfUnplacedFruits(self, fruits: List[int], baskets: List[int]) -> int:
        for f in fruits:
            for b in range(len(baskets)):
                if f <= baskets[b]:
                    del baskets[b]
                    break
        return len(baskets)

# Time : Beats 94.96 %
# Memo : Beats 84.21 %
# modifying
class Solution2:
    def numOfUnplacedFruits(self, fruits: List[int], baskets: List[int]) -> int:
        n = len(fruits)
        taken = 0
        for f in fruits:
            for b in range(n):
                if f <= baskets[b]:
                    baskets[b] = 0
                    taken += 1
                    break
        return n - taken