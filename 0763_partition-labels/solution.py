from typing import List

# Time : Beats 96.13%
# Memo : Beats 85.21%
# only track last occurance of char 
class Solution1:
    def partitionLabels(self, s: str) -> List[int]:
        last = {}
        for i,c in enumerate(s):
            last[c] = i
        res = []
        length, end = 0,0
        for i,c in enumerate(s):
            length +=1
            if end < last[c]: 
                end = last[c]
            if end == i:
                res.append(length)
                length = 0
        return res


# Time : Beats 96.13%
# Memo : Beats 36.45%
class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        res = []
        hash = {}
        chars = []
        for i in range(len(s)):
            char = s[i]
            if hash.get(char, False): # char not in hash
                hash[char][1] = i
            else:
                hash[char] = [i,i]
                chars.append(char)

        last = hash[chars[0]]
        for i in range(1,len(chars)):
            if hash[chars[i]][0] > last[1]: # no overlap
                last = hash[chars[i]]
                res.append(last[1] - last[0] + 1)
            else:
                last[1] = max(last[1],hash[chars[i]][1])
        res.append(last[1] - last[0] +1)
        return res
