# [3405. Count the Number of Arrays with K Matching Adjacent Elements](https://leetcode.com/problems/count-the-number-of-arrays-with-k-matching-adjacent-elements)


> Hard

- math
- combinatorics



## Question


<p>You are given three integers <code>n</code>, <code>m</code>, <code>k</code>. A <strong>good array</strong> <code>arr</code> of size <code>n</code> is defined as follows:</p>

<ul>
	<li>Each element in <code>arr</code> is in the <strong>inclusive</strong> range <code>[1, m]</code>.</li>
	<li><em>Exactly</em> <code>k</code> indices <code>i</code> (where <code>1 &lt;= i &lt; n</code>) satisfy the condition <code>arr[i - 1] == arr[i]</code>.</li>
</ul>

<p>Return the number of <strong>good arrays</strong> that can be formed.</p>

<p>Since the answer may be very large, return it <strong>modulo </strong><code>10<sup>9 </sup>+ 7</code>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">n = 3, m = 2, k = 1</span></p>

<p><strong>Output:</strong> <span class="example-io">4</span></p>

<p><strong>Explanation:</strong></p>

<ul>
	<li>There are 4 good arrays. They are <code>[1, 1, 2]</code>, <code>[1, 2, 2]</code>, <code>[2, 1, 1]</code> and <code>[2, 2, 1]</code>.</li>
	<li>Hence, the answer is 4.</li>
</ul>
</div>

<p><strong class="example">Example 2:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">n = 4, m = 2, k = 2</span></p>

<p><strong>Output:</strong> <span class="example-io">6</span></p>

<p><strong>Explanation:</strong></p>

<ul>
	<li>The good arrays are <code>[1, 1, 1, 2]</code>, <code>[1, 1, 2, 2]</code>, <code>[1, 2, 2, 2]</code>, <code>[2, 1, 1, 1]</code>, <code>[2, 2, 1, 1]</code> and <code>[2, 2, 2, 1]</code>.</li>
	<li>Hence, the answer is 6.</li>
</ul>
</div>

<p><strong class="example">Example 3:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">n = 5, m = 2, k = 0</span></p>

<p><strong>Output:</strong> <span class="example-io">2</span></p>

<p><strong>Explanation:</strong></p>

<ul>
	<li>The good arrays are <code>[1, 2, 1, 2, 1]</code> and <code>[2, 1, 2, 1, 2]</code>. Hence, the answer is 2.</li>
</ul>
</div>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= n &lt;= 10<sup>5</sup></code></li>
	<li><code>1 &lt;= m &lt;= 10<sup>5</sup></code></li>
	<li><code>0 &lt;= k &lt;= n - 1</code></li>
</ul>



## Solution

- time  : $O()$
- space : $O()$

---

- Given:
	- `n` : len of array
	- `m` : no. of candidate for each position to choose from
	- `k` : no. of good index (`arr[i] == arr[i-1]`)

- Intuition:
	- `nums[0]` will never be counted in `k`, therefore have `m` options
	- For the remaining `n-1` position, `k` of them can only have `1` option (same as `nums[i-1]`)
		- There are $C^{n-1}_{k}$ combination of good index
	- For the remaining `n-1-k` position, they can have `m-1` option (different with `nums[i-1]`)
	- Result = $m \cdot C^{n-1}_{k} \cdot (m-1)^{n-1-k}$

- Optimization:
	- Use "exponentiation by squaring"