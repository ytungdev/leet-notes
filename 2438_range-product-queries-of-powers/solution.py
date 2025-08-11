from typing import List

# Time : Beats 84.15 %
# Memo : Beats  6.10 %
class Solution:
    def productQueries(self, n: int, queries: List[List[int]]) -> List[int]:
        mod = 1000000007
        pref_sum = []
        val = 0
        while n > 0:
            if n%2:
                if not pref_sum:
                    pref_sum.append(val)
                else:
                    pref_sum.append(val+pref_sum[-1])
            n //= 2
            val += 1
        ret = []
        for l,r in queries:
            if l==0:
                ret.append((1 << pref_sum[r]) % mod)
            else:
                ret.append((1 << (pref_sum[r]-pref_sum[l-1])) % mod)
        return ret


# Time : Beats 83.54 %
# Memo : Beats  6.10 %
class Solution2:
    def productQueries(self, n: int, queries: List[List[int]]) -> List[int]:
         # # construct powers
        # powers = []
        # val = 1
        # while n > 0:
        #     if n%2:
        #         powers.append(val)
        #     n //= 2
        #     val <<= 1
        
        # # construct pref_prod
        # pref_prod = [arr[0]]
        # for i in range(1,len(arr)):
        #     pref_prod[i] = pref_prod[i-1]*arr[i]

        mod = 1000000007
        pref_prod = []
        val = 1
        while n > 0:
            if n%2:
                if not pref_prod:
                    pref_prod.append(val)
                else:
                    pref_prod.append(val*pref_prod[-1])
            n //= 2
            val <<= 1
        
        ret = []
        for l,r in queries:
            if l==0:
                ret.append(pref_prod[r] % mod)
            else:
                ret.append(pref_prod[r]//pref_prod[l-1] % mod)
        return ret



        
