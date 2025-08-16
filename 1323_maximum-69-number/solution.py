
# Time : Beats 100.0 %
# Memo : Beats 95.58 %
class Solution2:
    def maximum69Number (self, num: int) -> int:
        original = num
        order = 0
        target = -1
        while num > 0:
            if num % 10 == 6:
                target = order
            order += 1
            num //= 10
        return original if target == -1 else original + 3*10**target
    
# Time : Beats  5.32 %
# Memo : Beats 46.78 %
class Solution:
    def maximum69Number (self, num: int) -> int:
        num_str = str(num)
        for i in range(len(num_str)):
            if num_str[i] == '6':
                return int(num_str[:i]+'9'+num_str[i+1:])
        return num