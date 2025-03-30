# Time : Beats 37.47 %
# Memo : Beats 99.83 %

class Solution:
    def longestPalindrome(self, s: str) -> str:
        # eliminate even len
        s = "#"+"#".join(s)+"#"
        longest    = ""
        longestLen = 0
        for i in range(len(s)):
            L,R = i,i
            while L>=0 and R<len(s) and s[L] == s[R]:
                currLen = (R-L+1)
                if currLen > longestLen:
                    longestLen = currLen
                    longest = s[L:R]
                L -= 1
                R += 1

        return "".join([c for c in longest if c!='#'])

            