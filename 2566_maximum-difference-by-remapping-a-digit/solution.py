from typing import List

# Time : Beats 100.0 %
# Memo : Beats 78.64 %
class Solution:
    def minMaxDifference(self, num: int) -> int:
        num_str = str(num)

        max_replace = -1
        max_str = ''
        
        min_str = ''
        for i in num_str:
            if max_replace == -1:
                if i != '9':
                    max_replace = i
                max_str+='9'
            else:
                if i == max_replace:
                    max_str+='9'
                else:
                    max_str+=i
        
            if i == num_str[0]:
                min_str+='0'
            else:
                min_str+=i
                
        return int(max_str)-int(min_str)