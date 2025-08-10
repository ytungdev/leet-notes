from collections import Counter

# Time : Beats 100.0 %
# Memo : Beats 52.87 %
class Solution:
    def reorderedPowerOf2(self, n: int) -> bool:
        def serialize(num):
            return "".join(sorted(str(num)))
        
        target = serialize(n)
        for i in range(30):
            if serialize(1 << i) == target:
                return True
        return False


# Time : Beats 16.09 %
# Memo : Beats 52.87 %
class Solution2:
    def reorderedPowerOf2(self, n: int) -> bool:
        def check(n):
            return n & (n-1) == 0
        
        arr = []
        while n > 0:
            arr.append(n%10)
            n //= 10
        
        def permutate(comb, counter, n):
            if len(comb) == n:
                num = 0
                mult = 10**(n-1)
                for n in comb:
                    num += n*mult
                    mult //= 10
                return check(num)
            for num in counter:
                if not comb and num == 0:
                    continue
                if counter[num] > 0:
                    comb.append(num)
                    counter[num] -= 1
                    if permutate(comb, counter,n):
                        return True
                    comb.pop()
                    counter[num] += 1
            return False
        
        return permutate([], Counter(arr), len(arr))