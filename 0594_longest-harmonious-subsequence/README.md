# [0594. Longest Harmonious Subsequence](https://leetcode.com/problems/longest-harmonious-subsequence)


> Easy

- array
- hash-table
- sliding-window
- sorting
- counting



## Question


<p>We define a harmonious array as an array where the difference between its maximum value and its minimum value is <b>exactly</b> <code>1</code>.</p>

<p>Given an integer array <code>nums</code>, return the length of its longest harmonious <span data-keyword="subsequence-array">subsequence</span> among all its possible subsequences.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">nums = [1,3,2,2,5,2,3,7]</span></p>

<p><strong>Output:</strong> <span class="example-io">5</span></p>

<p><strong>Explanation:</strong></p>

<p>The longest harmonious subsequence is <code>[3,2,2,2,3]</code>.</p>
</div>

<p><strong class="example">Example 2:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">nums = [1,2,3,4]</span></p>

<p><strong>Output:</strong> <span class="example-io">2</span></p>

<p><strong>Explanation:</strong></p>

<p>The longest harmonious subsequences are <code>[1,2]</code>, <code>[2,3]</code>, and <code>[3,4]</code>, all of which have a length of 2.</p>
</div>

<p><strong class="example">Example 3:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">nums = [1,1,1,1]</span></p>

<p><strong>Output:</strong> <span class="example-io">0</span></p>

<p><strong>Explanation:</strong></p>

<p>No harmonic subsequence exists.</p>
</div>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= nums.length &lt;= 2 * 10<sup>4</sup></code></li>
	<li><code>-10<sup>9</sup> &lt;= nums[i] &lt;= 10<sup>9</sup></code></li>
</ul>



## Solution

- time  : $O(N+D)$, where `D` is the number of distinct number in `nums`
	- Construction of `Counter()` take $O(N)$
	- Comparing all possible subsequence take $O(D)$
- space : $O(D)$

---

- Objective:
	- Harmonious array is defined as array `arr` where `max(arr) - min(arr) == 1`
	- Return longest length of harmonious array among all subsequence of `nums`
- Intuition:
	- Order of subsequnce do not matter, therefore we can represent `nums` as `Counter(nums)`.
	- Harmonious array is the array containing `num` and `num+1`
		- A array `arr` is not harmonious if `arr` only contain `num`
	- For each distinct number `num`,  
		- If `num+1 in nums`, harmonious array with `min(arr)==num` exist 
		- Max length of such harmonious array = `nums.count(num) + nums.count(num+1)`
