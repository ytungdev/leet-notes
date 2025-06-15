from typing import List

# Time : Beats 100.0 %
# Memo : Beats 57.69 %
class Solution:
    def maxDiff(self, num: int) -> int:
        num_str = str(num)
        n = len(num_str)

        max_replace = -1
        max_str = ''
        for i in num_str:
            if max_replace == -1:
                if i!='9':
                    max_replace = i
                max_str += '9'
            else:
                if i == max_replace:
                    max_str += '9'
                else:
                    max_str += i
        if num_str[0] == '1':
            i = 1
            while i < n:
                if num_str[i] != '1' and num_str[i] != '0':
                    min_str = num_str.replace(num_str[i],'0')
                    break
                i += 1
            if i==n:
                min_str = num_str
        else:
            min_str = num_str.replace(num_str[0],'1')

        return int(max_str) - int(min_str)