from typing import List

# Time : Beats 97.81 % -- O(N)
# Memo : Beats  7.79 % -- O(N)
class Solution1:
    def countLargestGroup(self, n: int) -> int:
        dp = {0:0} # store grp of each num
        freq = [0]*36 # store freq of each grp
        for num in range(1,n+1):
            q,r = num // 10, num % 10 # (//,%) faster than divmod()
            dp[num] = r + dp[q]
            freq[dp[num]-1] += 1
        return freq.count(max(freq))
    

# Time : Beats 80.29 % -- O(NlogN)
# Memo : Beats 41.12 % -- O(logN)
class Solution:
    def countLargestGroup(self, n: int) -> int:
        def find_grp(num): # O(logN)
            grp = 0
            while num>=1:
                grp += num % 10
                num //= 10
            return grp
        grps = [0]*37
        max_size = 0
        for i in range(1,n+1): # O(N)
            grp = find_grp(i)
            grps[grp] += 1
            if grps[grp] > max_size:
                max_size = grps[grp]
        ret = 0
        for v in grps: # O(logN)
            if v == max_size:
                ret += 1
        return ret