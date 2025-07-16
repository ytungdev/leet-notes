# [3201. Find the Maximum Length of Valid Subsequence I](https://leetcode.com/problems/find-the-maximum-length-of-valid-subsequence-i)


> Medium

- array
- dynamic-programming



## Question


You are given an integer array <code>nums</code>.
<p>A <span data-keyword="subsequence-array">subsequence</span> <code>sub</code> of <code>nums</code> with length <code>x</code> is called <strong>valid</strong> if it satisfies:</p>

<ul>
	<li><code>(sub[0] + sub[1]) % 2 == (sub[1] + sub[2]) % 2 == ... == (sub[x - 2] + sub[x - 1]) % 2.</code></li>
</ul>

<p>Return the length of the <strong>longest</strong> <strong>valid</strong> subsequence of <code>nums</code>.</p>

<p>A <strong>subsequence</strong> is an array that can be derived from another array by deleting some or no elements without changing the order of the remaining elements.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">nums = [1,2,3,4]</span></p>

<p><strong>Output:</strong> <span class="example-io">4</span></p>

<p><strong>Explanation:</strong></p>

<p>The longest valid subsequence is <code>[1, 2, 3, 4]</code>.</p>
</div>

<p><strong class="example">Example 2:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">nums = [1,2,1,1,2,1,2]</span></p>

<p><strong>Output:</strong> 6</p>

<p><strong>Explanation:</strong></p>

<p>The longest valid subsequence is <code>[1, 2, 1, 2, 1, 2]</code>.</p>
</div>

<p><strong class="example">Example 3:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">nums = [1,3]</span></p>

<p><strong>Output:</strong> <span class="example-io">2</span></p>

<p><strong>Explanation:</strong></p>

<p>The longest valid subsequence is <code>[1, 3]</code>.</p>
</div>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>2 &lt;= nums.length &lt;= 2 * 10<sup>5</sup></code></li>
	<li><code>1 &lt;= nums[i] &lt;= 10<sup>7</sup></code></li>
</ul>



## Solution

- time  : $O(N)$
- space : $O(1)$

---

- Intuition:
	- There are 4 type of valid `sub`(0 indicate even number, 1 indicate odd number):
		1. `00000..` : all even
		2. `11111..` : all odd
		3. `01010..` : alternating, start with even
		4. `10101..` : alternating, start with odd
	- For alternating `sub`, max length always include `nums[0]`
		- Type 3 and 4 can be combined as alternating `sub`
	- `all_odd = len(nums) - all_even`
- Implementation:
	- Keep track of max length in each type:
		- `all_even`, `alter`
	- Track starting parity for alternating `sub` : `parity = nums[0]%2`
	- Iterate `num` in `nums`:
		- if `num` is odd: `all_odd+=1`
		- if parity of `num` equal `parity` : `alter+=1` and `parity ^= 1`
	- return `max(all_even,len(nums)-all_even,alter)`
