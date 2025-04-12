from typing import List

# Time : Beats 97.55 %
# Memo : Beats 35.31 %
class Solution2:
    def countSymmetricIntegers(self, low: int, high: int) -> int:
        if high < 1001:
            # 1 <= x <= 99
            return high // 11 - (low-1)//11
        else:
            count = 0
            # 1 <= x <= 99
            if low < 100:
                count += 9 - (low-1)//11
            # 1001 <= x <= 9999
            for n in range(max(low,1001),high+1):
                L = n//1000 + n//100%10
                R = n//10%10 + n%10
                if L==R:
                    print(n)
                    count += 1
            return count

# Time : Beats 88.16 %
# Memo : Beats 13.06 %
class Solution:
    def countSymmetricIntegers(self, low: int, high: int) -> int:
        def digits(num):
            arr = []
            while num > 0:
                arr.append(num%10)
                num //= 10
            return arr

        count = 0
        for n in range(max(low,11),high+1):
            num = digits(n)
            l = len(num)
            if l%2:
                continue
            if sum(num[0:l//2]) == sum(num[l//2:]):
                count += 1
        return count
