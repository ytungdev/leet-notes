# [2140. Solving Questions With Brainpower](https://leetcode.com/problems/solving-questions-with-brainpower)


> Medium

- array
- dynamic-programming



## Question


<p>You are given a <strong>0-indexed</strong> 2D integer array <code>questions</code> where <code>questions[i] = [points<sub>i</sub>, brainpower<sub>i</sub>]</code>.</p>

<p>The array describes the questions of an exam, where you have to process the questions <strong>in order</strong> (i.e., starting from question <code>0</code>) and make a decision whether to <strong>solve</strong> or <strong>skip</strong> each question. Solving question <code>i</code> will <strong>earn</strong> you <code>points<sub>i</sub></code> points but you will be <strong>unable</strong> to solve each of the next <code>brainpower<sub>i</sub></code> questions. If you skip question <code>i</code>, you get to make the decision on the next question.</p>

<ul>
	<li>For example, given <code>questions = [[3, 2], [4, 3], [4, 4], [2, 5]]</code>:

	<ul>
		<li>If question <code>0</code> is solved, you will earn <code>3</code> points but you will be unable to solve questions <code>1</code> and <code>2</code>.</li>
		<li>If instead, question <code>0</code> is skipped and question <code>1</code> is solved, you will earn <code>4</code> points but you will be unable to solve questions <code>2</code> and <code>3</code>.</li>
	</ul>
	</li>
</ul>

<p>Return <em>the <strong>maximum</strong> points you can earn for the exam</em>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> questions = [[3,2],[4,3],[4,4],[2,5]]
<strong>Output:</strong> 5
<strong>Explanation:</strong> The maximum points can be earned by solving questions 0 and 3.
- Solve question 0: Earn 3 points, will be unable to solve the next 2 questions
- Unable to solve questions 1 and 2
- Solve question 3: Earn 2 points
Total points earned: 3 + 2 = 5. There is no other way to earn 5 or more points.
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> questions = [[1,1],[2,2],[3,3],[4,4],[5,5]]
<strong>Output:</strong> 7
<strong>Explanation:</strong> The maximum points can be earned by solving questions 1 and 4.
- Skip question 0
- Solve question 1: Earn 2 points, will be unable to solve the next 2 questions
- Unable to solve questions 2 and 3
- Solve question 4: Earn 5 points
Total points earned: 2 + 5 = 7. There is no other way to earn 7 or more points.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= questions.length &lt;= 10<sup>5</sup></code></li>
	<li><code>questions[i].length == 2</code></li>
	<li><code>1 &lt;= points<sub>i</sub>, brainpower<sub>i</sub> &lt;= 10<sup>5</sup></code></li>
</ul>



## Solution

- time  : $O(N)$
- space : $O(N)$

---

- bottom-up Dynamic Programming with memoisation

- Idea:
	- explores two option finish/skip the question and return max point among the two option for each question
	- start the iteration from last question to first question
		- Given that last question only have one possible way to score (finish the question)
	- return max possible point of first question
- Implementation:
	- Array iteration **O(N)**
		- use array `dp` to memoize max possible point that can acheive at question `i` as `dp[i]`
			- set default score of each index to `0`
			- set default score of last element to point of last question
		- iterate throgh `question` from second last element to first element
			- find index of next available question `next_q`
				- `i + question[i][0] + 1`
			- find possible point finishing this question `finish`
				- if further question is available, `question[i][0] + dp[next_q]`
				- if no further question is available, `question[i][0]`
			- find possible point skipping this question `skip`
				- `dp[i+1]`
			- set `dp[i]` to best option
		- return `dp[0]`
	- Recursion **O(N)**
		- use array `max_score` to memoize max possible point that can acheive at question `i` as `max_socre[i]`
			- set default score of each index to `0`
		- define function `find_max(i)`
			- if `i` out of bound (`>len(nums)`) return `0`
			- if `max_score[i]` already been calculated(`!= 0`), return `max_score[i]`
			- else return max among 
				- `find_max[i+1]` (skip this question)
				- `question[i][0] + find_max[i + skip +1]` (finish this question, and get max possible point from next question available)
		- iterate throgh `question` from end of array to start of array
		- return `max_score[0]`
