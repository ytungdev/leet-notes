# [2799. Count Complete Subarrays in an Array](https://leetcode.com/problems/count-complete-subarrays-in-an-array)


> Medium

- array
- hash-table
- sliding-window



## Question


<p>You are given an array <code>nums</code> consisting of <strong>positive</strong> integers.</p>

<p>We call a subarray of an array <strong>complete</strong> if the following condition is satisfied:</p>

<ul>
	<li>The number of <strong>distinct</strong> elements in the subarray is equal to the number of distinct elements in the whole array.</li>
</ul>

<p>Return <em>the number of <strong>complete</strong> subarrays</em>.</p>

<p>A <strong>subarray</strong> is a contiguous non-empty part of an array.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> nums = [1,3,1,2,2]
<strong>Output:</strong> 4
<strong>Explanation:</strong> The complete subarrays are the following: [1,3,1,2], [1,3,1,2,2], [3,1,2] and [3,1,2,2].
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> nums = [5,5,5,5]
<strong>Output:</strong> 10
<strong>Explanation:</strong> The array consists only of the integer 5, so any subarray is complete. The number of subarrays that we can choose is 10.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= nums.length &lt;= 1000</code></li>
	<li><code>1 &lt;= nums[i] &lt;= 2000</code></li>
</ul>



## Solution

- time  : $O(N)$
- space : $O(N)$

---

- Technique : sliding window
- Idea:
	- Keep track of frequency of digit in current window`freq` and return value `count`
	- Use two pointer `L,R` to iterate throguh `nums`, for each `L`:
		- when `L>0`, remove `nums[L-1]` in `freq` and add `nums[R]`
	- Starting at index `L,R=0`, `R++` until current subarray is complete
		- when complete, `len(freq) = len(set(nums))`
	- Once the subarray is completed, extending current subarray is also complete
		- `count += len(nums) - (R+1) + 1`
			- `[1 3 1 2] 2 1` : `1312`, `13122` and `131221`
	- After reaching a completed subarray, `L++` until reaching `L=len(N)`