from typing import List

# Time : Beats 76.61 %
# Memo : Beats 47.37 %
class Solution:
    def getWordsInLongestSubsequence(self, words: List[str], groups: List[int]) -> List[str]:
        def pass_checking(i,j): #O(N)
            if groups[i] == groups[j]:
                return False
            if len(words[i]) != len(words[j]):
                return False
            res = 0
            for n in range(len(words[i])):
                if words[i][n] != words[j][n]:
                    if res == 1:
                        return False
                    res += 1
            return res == 1

        n = len(groups)
        dp_l = [1]*n
        dp_a = [[w] for w in words]
        
        max_l, best = 1,0

        for R in range(1,n):
            best_l = dp_l[R]
            for L in range(R-1,-1,-1):
                if pass_checking(L,R) and dp_l[L]+1 > best_l:
                    best_l = dp_l[L]+1
                    dp_l[R] = best_l
                    dp_a[R] = dp_a[L] + [words[R]]
                    if dp_l[R] > max_l:
                        max_l = dp_l[R]
                        best = R
        
                    
        return dp_a[best]