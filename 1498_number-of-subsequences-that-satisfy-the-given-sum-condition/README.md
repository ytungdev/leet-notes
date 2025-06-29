# [1498. Number of Subsequences That Satisfy the Given Sum Condition](https://leetcode.com/problems/number-of-subsequences-that-satisfy-the-given-sum-condition)


> Medium

- array
- two-pointers
- binary-search
- sorting



## Question


<p>You are given an array of integers <code>nums</code> and an integer <code>target</code>.</p>

<p>Return <em>the number of <strong>non-empty</strong> subsequences of </em><code>nums</code><em> such that the sum of the minimum and maximum element on it is less or equal to </em><code>target</code>. Since the answer may be too large, return it <strong>modulo</strong> <code>10<sup>9</sup> + 7</code>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> nums = [3,5,6,7], target = 9
<strong>Output:</strong> 4
<strong>Explanation:</strong> There are 4 subsequences that satisfy the condition.
[3] -&gt; Min value + max value &lt;= target (3 + 3 &lt;= 9)
[3,5] -&gt; (3 + 5 &lt;= 9)
[3,5,6] -&gt; (3 + 6 &lt;= 9)
[3,6] -&gt; (3 + 6 &lt;= 9)
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> nums = [3,3,6,8], target = 10
<strong>Output:</strong> 6
<strong>Explanation:</strong> There are 6 subsequences that satisfy the condition. (nums can have repeated numbers).
[3] , [3] , [3,3], [3,6] , [3,6] , [3,3,6]
</pre>

<p><strong class="example">Example 3:</strong></p>

<pre>
<strong>Input:</strong> nums = [2,3,3,4,6,7], target = 12
<strong>Output:</strong> 61
<strong>Explanation:</strong> There are 63 non-empty subsequences, two of them do not satisfy the condition ([6,7], [7]).
Number of valid subsequences (63 - 2 = 61).
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= nums.length &lt;= 10<sup>5</sup></code></li>
	<li><code>1 &lt;= nums[i] &lt;= 10<sup>6</sup></code></li>
	<li><code>1 &lt;= target &lt;= 10<sup>6</sup></code></li>
</ul>



## Solution

- time  : $O(N \cdot logN + N)$
	- `nums.sort()` take $O(N \cdot logN)$
	- Iteratating min/max pair with two pointer take $O(N)$
- space : $O(N)$
	- To store value of $2^i$ for better computation

---

- Objectives:
	- Find subsequence `sub` of `nums` with:
		- length `n>0`
		- `min(sub) + max(sub) <= target`
	- Return number of such subsequence
- Intuition:
	- Even though the objective is to find subsequence, order of element do not matter in result
		- Sorting `nums` is feasible
	- After sorting `nums`, we can find valid min/max pair in `nums` with two-pointer
		- Starting with `L,R = 0,n-1`
		- If `nums[L] + nums[R] <= target` : `L++`
			- Add number of sequence that have min value `nums[L]` : `ret += 2**(R-L)`
			- For subsequnce of length `l`, there are `2**(l-1)` valid subsequence containing `nums[L]`
		- Else : `R--`
		- Until `L<=R` to also test for array only containing 1 element
- Optimization:
	- Pre-compute value of `2**i % mod`