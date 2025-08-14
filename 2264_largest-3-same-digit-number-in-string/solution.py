
# Time : Beats 100.0 %
# Memo : Beats 17.53 %
class Solution2:
    def largestGoodInteger(self, num: str) -> str:
        ret = ""
        i = 0
        while i < len(num)-2:
            if num[i] == num[i+1] == num[i+2]:
                ret = max(ret, num[i]*3)
                i = i+3
            else:
                i+=1
        return ret

# Time : Beats 67.45 %
# Memo : Beats 87.48 %
class Solution:
    def largestGoodInteger(self, num: str) -> str:
        num += "-"
        
        ret = ""
        curr = ""
        freq = 0
        for n in num:
            if n != curr:
                if freq >= 3 and curr > ret:
                    ret = curr
                curr = n
                freq = 1
            else:
                freq += 1
        return ret*3