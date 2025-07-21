from typing import List

# Time : Beats 82.49 %
# Memo : Beats 65.03 %
class Solution:
    def removeSubfolders(self, folder: List[str]) -> List[str]:
        folder.sort()
        ret = [folder[0]]
        for i in range(1,len(folder)):
            if folder[i].startswith(f'{ret[-1]}/'):
                continue
            ret.append(folder[i])
        return ret
