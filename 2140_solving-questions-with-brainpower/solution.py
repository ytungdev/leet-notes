from typing import List

# Time : Beats 47.93 %
# Memo : Beats 88.13 %

class Solution:
    def mostPoints(self, questions: List[List[int]]) -> int:
        q_no = len(questions)
        max_scores = [0]*q_no
        def max_scores_at(i):
            if i >= q_no:
                return 0
            if max_scores[i] != 0:
                return max_scores[i]
            return max(questions[i][0] + max_scores_at(i+questions[i][1]+1), max_scores_at(i+1))
        
        for i in range(q_no-1,-1,-1):
            max_scores[i] = max_scores_at(i)

        return max(max_scores)
