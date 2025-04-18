# Time : Beats 97.10 %
# Memo : Beats 61.49 %
class Solution:
    def countAndSay(self, n: int) -> str:
        def rle(s):
            curr = s[0]
            cnt = 1
            ret = ''
            for chr in s[1:]:
                if chr == curr:
                    cnt += 1
                else:
                    ret += f'{cnt}{curr}'
                    curr = chr
                    cnt = 1
            return f'{ret}{cnt}{curr}'
        i = 1
        ret = '1'
        while i < n:
            ret = rle(ret)
            i+=1
        return ret