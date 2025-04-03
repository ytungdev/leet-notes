from typing import List

# Time : Beats 92.75 %
# Memo : Beats 44.60 %
# dp with array
class Solution1:
    def mostPoints(self, questions: List[List[int]]) -> int:
        n = len(questions)
        dp = [0] * (n-1)
        dp.append(questions[-1][0]) # last question only have one possible max points

        for i in range(n-2,-1,-1):
            next_q = i + questions[i][1] + 1
            finish = questions[i][0] + (dp[next_q] if next_q < n else 0)
            skip = dp[i+1]
            dp[i] = max(skip, finish)
        
        return dp[0]
    
# Time : Beats 47.93 %
# Memo : Beats 88.13 %
# dp with recursion
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
