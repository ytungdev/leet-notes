# [2616. Minimize the Maximum Difference of Pairs](https://leetcode.com/problems/minimize-the-maximum-difference-of-pairs)


> Medium

- array
- binary-search
- greedy



## Question


<p>You are given a <strong>0-indexed</strong> integer array <code>nums</code> and an integer <code>p</code>. Find <code>p</code> pairs of indices of <code>nums</code> such that the <strong>maximum</strong> difference amongst all the pairs is <strong>minimized</strong>. Also, ensure no index appears more than once amongst the <code>p</code> pairs.</p>

<p>Note that for a pair of elements at the index <code>i</code> and <code>j</code>, the difference of this pair is <code>|nums[i] - nums[j]|</code>, where <code>|x|</code> represents the <strong>absolute</strong> <strong>value</strong> of <code>x</code>.</p>

<p>Return <em>the <strong>minimum</strong> <strong>maximum</strong> difference among all </em><code>p</code> <em>pairs.</em> We define the maximum of an empty set to be zero.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> nums = [10,1,2,7,1,3], p = 2
<strong>Output:</strong> 1
<strong>Explanation:</strong> The first pair is formed from the indices 1 and 4, and the second pair is formed from the indices 2 and 5. 
The maximum difference is max(|nums[1] - nums[4]|, |nums[2] - nums[5]|) = max(0, 1) = 1. Therefore, we return 1.
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> nums = [4,2,1,2], p = 1
<strong>Output:</strong> 0
<strong>Explanation:</strong> Let the indices 1 and 3 form a pair. The difference of that pair is |2 - 2| = 0, which is the minimum we can attain.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= nums.length &lt;= 10<sup>5</sup></code></li>
	<li><code>0 &lt;= nums[i] &lt;= 10<sup>9</sup></code></li>
	<li><code>0 &lt;= p &lt;= (nums.length)/2</code></li>
</ul>



## Solution

- time  : $O(N \cdot logN +  N \cdot logM)$, where `M` is the maximum value in `nums`
	- Sorting `nums` take $O(N \cdot logN)$
	- Binary search for valid difference take $O(N \cdot logM)$
		- $O(logM)$ attempt
		- Each attempt take $O(N)$
- space : $O(1)$

---

- Intuition:
	- Sort the array so that paring adjacent element result in minimum differences
	- Denote `f(d,p) = True` if possible to find `p` pair with max diff `d`
	- If `f(d,p)` is true, `f(d+1,p)` also true
    - If `f(d,p)` is false, `f(d-1,p)` also false
	- Therefore we can test for valid `d` with binary search to effectively narrow down solution space
- Implementation:
	- Sort `nums` -- $O(N \cdot logN)$
	- Define `test(d,p,nums)` to check `f(d,p)` for given array `nums` -- $O(N)$
		- For each element `nums[i]`, `count+=1` if `nums[i+1] - nums[i] >= d`
		- Return `count>=p`
	- Binary search valid `d`: -- $O(log M)$
		- lower bound of `d` is `0`
		- upper bound of `d` is `max(nums) - min(nums)`
		- Initiate `L,R` as lower and upper bound
		- In each iteration:
			- `M = (L+R)//2`
			- `test(M,p,nums)`
				- If `True`: try smaller `d` (`R=M`)
				- If `False`: try larger `d` (`L=M+1`)