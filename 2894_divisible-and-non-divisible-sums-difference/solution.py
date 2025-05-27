from typing import List

# Time : Beats 100.0 %
# Memo : Beats 98.41 %
# sum of seq
class Solution:
    def differenceOfSums(self, n: int, m: int) -> int:
        '''
        See README.md
        '''
        k = n//m
        return (1+n)*(n)//2 - (1+k)*m*k
    
# Time : Beats 100.0 %
# Memo : Beats 67.05 %
# process multiple of m
class Solution2:
    def differenceOfSums(self, n: int, m: int) -> int:
        '''
        1 -- m -- 2m -- 3m .. km -- n
            
        1,2,3,4,5,6,7,8,9,10
            ^     ^     ^  
                            +
                    + + -
              + + -
        + + -
        '''
        def seq_sum(s,e):
            return (s+e)*(e-s+1)//2
        res = 0
        multiple = n//m*m
        res += seq_sum(multiple+1, n)
        while multiple:
            res -= multiple
            res += seq_sum(multiple-m+1,multiple-1)
            multiple -= m
        return res
    
# Time : Beats 60.78 %
# Memo : Beats 39.75 %
# naive
class Solution:
    def differenceOfSums(self, n: int, m: int) -> int:
        '''
        n1 = a+b+c for num%m != 0
        n2 = i+j+k for num%m == 0
        n1 - n2 = a+b+c-i-j-k
        '''
        res = 0
        for num in range(1,n+1):
            if num % m:
                res += num
            else:
                res -= num
        return res