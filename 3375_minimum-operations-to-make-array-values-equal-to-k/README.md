# [3375. Minimum Operations to Make Array Values Equal to K](https://leetcode.com/problems/minimum-operations-to-make-array-values-equal-to-k)


> Easy

- array
- hash-table



## Question


<p>You are given an integer array <code>nums</code> and an integer <code>k</code>.</p>

<p>An integer <code>h</code> is called <strong>valid</strong> if all values in the array that are <strong>strictly greater</strong> than <code>h</code> are <em>identical</em>.</p>

<p>For example, if <code>nums = [10, 8, 10, 8]</code>, a <strong>valid</strong> integer is <code>h = 9</code> because all <code>nums[i] &gt; 9</code>&nbsp;are equal to 10, but 5 is not a <strong>valid</strong> integer.</p>

<p>You are allowed to perform the following operation on <code>nums</code>:</p>

<ul>
	<li>Select an integer <code>h</code> that is <em>valid</em> for the <strong>current</strong> values in <code>nums</code>.</li>
	<li>For each index <code>i</code> where <code>nums[i] &gt; h</code>, set <code>nums[i]</code> to <code>h</code>.</li>
</ul>

<p>Return the <strong>minimum</strong> number of operations required to make every element in <code>nums</code> <strong>equal</strong> to <code>k</code>. If it is impossible to make all elements equal to <code>k</code>, return -1.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">nums = [5,2,5,4,5], k = 2</span></p>

<p><strong>Output:</strong> <span class="example-io">2</span></p>

<p><strong>Explanation:</strong></p>

<p>The operations can be performed in order using valid integers 4 and then 2.</p>
</div>

<p><strong class="example">Example 2:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">nums = [2,1,2], k = 2</span></p>

<p><strong>Output:</strong> <span class="example-io">-1</span></p>

<p><strong>Explanation:</strong></p>

<p>It is impossible to make all the values equal to 2.</p>
</div>

<p><strong class="example">Example 3:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">nums = [9,7,5,3], k = 1</span></p>

<p><strong>Output:</strong> <span class="example-io">4</span></p>

<p><strong>Explanation:</strong></p>

<p>The operations can be performed using valid integers in the order 7, 5, 3, and 1.</p>
</div>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= nums.length &lt;= 100 </code></li>
	<li><code>1 &lt;= nums[i] &lt;= 100</code></li>
	<li><code>1 &lt;= k &lt;= 100</code></li>
</ul>


## Solution 

- Objective:
	- return `-1` if any element is smaller than `k`
	- return step from largest element to `k`
		- find distinct integer greater than `k` in array

#### Method 2 : set

- time  : $O(N)$
- space : $O(1)$

---

- Idea:
	- Return `-1` if `min(nums)` < `k` -- $O(N)$
	- Convert `nums` to set
		- set lookup and insert of set is $O(1)$
	- Store seen elemnt in `res`
	- Iterate from first element to last element -- $O(N)$
		- if current element `nums[i]` not in `res` and greater than `k`, 
			- add `nums[i]` to `res`
	- return length of `res`

#### Method 1 : sort

- time  : $O(N \log N)$
- space : $O(1)$

---

- Idea:
	- Sort array in reverse order  -- $O(N \log N)$
	- Return `-1` if smallest element `nums[-1]` less than `k`
	- Store last integer `last` and result as `res`
	- Iterate from first element to last element -- $O(N)$
		- if current element `nums[i]` not equal to `last`, 
			- `res++`
			- `last` = `nums[i]`
		- if current element `nums[i]` equal `k` return `res`
	- If last element not equal to `k` return `res++`