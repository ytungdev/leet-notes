# [0342. Power of Four](https://leetcode.com/problems/power-of-four)


> Easy

- math
- bit-manipulation
- recursion



## Question


<p>Given an integer <code>n</code>, return <em><code>true</code> if it is a power of four. Otherwise, return <code>false</code></em>.</p>

<p>An integer <code>n</code> is a power of four, if there exists an integer <code>x</code> such that <code>n == 4<sup>x</sup></code>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<pre><strong>Input:</strong> n = 16
<strong>Output:</strong> true
</pre><p><strong class="example">Example 2:</strong></p>
<pre><strong>Input:</strong> n = 5
<strong>Output:</strong> false
</pre><p><strong class="example">Example 3:</strong></p>
<pre><strong>Input:</strong> n = 1
<strong>Output:</strong> true
</pre>
<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>-2<sup>31</sup> &lt;= n &lt;= 2<sup>31</sup> - 1</code></li>
</ul>

<p>&nbsp;</p>
<strong>Follow up:</strong> Could you solve it without loops/recursion?


## Solution

## Approach 1 - log with iteration

- time  : $O(logN)$
- space : $O(1)$

---

- While `n%4 == 0`, `n//=4`
- Else, return `False`
- Return `True` if `n` become `0`

## Approach 2 - precomputed bit mask

- time  : $O(1)$
- space : $O(1)$

---

- Power of 4 is always power of 2, hence will pass power of 2 check
	- `return n & (n-1) == 0`
- Power of 4 have the following pattern:
	- Only one bit is a 1
	- The one is in odd number place
		- `4^0 = 1`
		- `4^1 = 100`
		- `4^2 = 10000`
- Max power of 4 in constraint:
	- $4^n <= 2^{31} - 1$, `n=15`
- Let `mask` be the XOR of all power of 4 within constraint (`1431655765`)
	- `for i in range(16): res ^= 4**i`
- `n` is a power of 4 if:
	- `n & mask = n` or `n | mask == mask`
	- `n>0`
	- `n` is a power of 2